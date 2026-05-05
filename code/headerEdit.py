import csv
import os
import re
import sys
from xml.etree import ElementTree as ET

def create_header_text(work_info, partic_desc_str):
    # Optional elements
    isni_idno = f'<idno type="ISNI">{work_info["ISNI"]}</idno>' if work_info['ISNI'] and work_info['ISNI'] != '없음' else ''
    wikisource_idno = f'                    <idno type="wikisource">{work_info["링크"]}</idno>' if work_info['링크'] and work_info['링크'] != '없음' else ''
    wikidata_idno = f'                    <idno type="wikidata">{work_info["작품id"]}</idno>' if work_info['작품id'] and work_info['작품id'] != '없음' else ''
    wikidata_url_idno = f'                    <idno type="wikidata-url">{work_info["작품id 링크"]}</idno>' if work_info['작품id 링크'] and work_info['작품id 링크'] != '없음' else ''
    
    encykorea_bibl = ""
    if work_info['민족문화대백과사전 id'] and work_info['민족문화대백과사전 id'] != '없음':
        encykorea_bibl = f'''
                <bibl type="reference" xml:lang="ko">
                    <title level="a">{work_info['작품 제목']}</title>
                    <idno type="encykorea-id">{work_info['민족문화대백과사전 id']}</idno>
                    <idno type="encykorea">https://encykorea.aks.ac.kr/Article/{work_info['민족문화대백과사전 id']}</idno>
                </bibl>'''

    # teiHeader 템플릿 생성
    header_template = f"""    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title>{work_info['작품 제목']}</title>
                <author>{work_info['저자']}{isni_idno}</author>
            </titleStmt>

            <publicationStmt>
                <publisher>한국학중앙연구원 인문정보학과</publisher>
            </publicationStmt>

            <sourceDesc>
                <bibl type="digitalSource" xml:lang="ko">
                    <title level="a">{work_info['작품 제목']}</title>
                    <author>{work_info['저자']}</author>
                    <publisher>Wikisource(한국어)</publisher>
{wikisource_idno if wikisource_idno else ''}
{wikidata_idno if wikidata_idno else ''}
{wikidata_url_idno if wikidata_url_idno else ''}
                </bibl>
{encykorea_bibl if encykorea_bibl else ''}
            </sourceDesc>
        </fileDesc>

        <encodingDesc>
            <projectDesc>
                <p>본 전자본은 위키문헌에 공개된 텍스트를 바탕으로 TEI P5 지침(TEI Lite)에 따라 구조화함.</p>
            </projectDesc>
        </encodingDesc>

        <profileDesc>
            <langUsage>
                <language ident="ko">한국어</language>
            </langUsage>
            <textClass>
                <keywords scheme="local">
                    <term>근현대 한국문학</term>
                </keywords>
            </textClass>
{partic_desc_str if partic_desc_str else ''}
        </profileDesc>
    </teiHeader>"""
    
    return header_template
    
def get_work_title_and_partic_desc(xml_file_path):
    try:
        # Register the namespace to handle it correctly
        ET.register_namespace('', "http://www.tei-c.org/ns/1.0")
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
        
        title_element = root.find('.//tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title', ns)
        title = title_element.text if title_element is not None else None
        
        partic_desc_element = root.find('.//tei:teiHeader/tei:profileDesc/tei:particDesc', ns)
        partic_desc_str = ET.tostring(partic_desc_element, encoding='unicode') if partic_desc_element is not None else None
        
        return title, partic_desc_str
    except Exception as e:
        print(f"Error parsing XML: {e}")
    return None, None

def process_single_xml_file(input_xml_path, output_xml_path, csv_file_path='작품목록.csv'):
    # CSV 파일 읽기
    works = {}
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                works[row['작품 제목']] = row
    except FileNotFoundError:
        print(f"Error: {csv_file_path} not found.")
        return
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    work_title, partic_desc_str = get_work_title_and_partic_desc(input_xml_path)
    if not work_title:
        print(f"Error: Could not extract work title from {input_xml_path}.")
        return

    if work_title in works:
        try:
            # 파일 전체 내용 읽기
            with open(input_xml_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # teiHeader 부분 찾기 및 교체
            pattern = r'<teiHeader>.*?</teiHeader>'
            new_header = create_header_text(works[work_title], partic_desc_str)
            
            # re.DOTALL 플래그를 사용하여 개행 문자도 포함하여 매칭
            new_content = re.sub(pattern, new_header, content, flags=re.DOTALL)
            
            # 수정된 내용 저장
            with open(output_xml_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f'{input_xml_path} 파일의 teiHeader가 성공적으로 수정되어 {output_xml_path} (으)로 저장되었습니다.')
        
        except Exception as e:
            print(f'오류: {input_xml_path} 파일 처리 중 문제가 발생했습니다: {str(e)}')
    else:
        print(f'경고: "{work_title}"에 대한 정보를 CSV 파일에서 찾을 수 없습니다.')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python headerEdit.py <input_xml_file> <output_xml_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_single_xml_file(input_file, output_file)