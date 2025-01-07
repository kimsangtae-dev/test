from bs4 import BeautifulSoup

def parse_pre_tag_from_html(input_html_file, output_txt_file):
    try:
        # HTML 파일 읽기
        with open(input_html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(html_content, 'html.parser')


        # <pre> 태그 중 id="console"인 태그의 텍스트 추출
        pre_tag = soup.find('pre', id='console')
        if pre_tag:
            console_text = pre_tag.get_text()
        else:
            console_text = ""  # id="console" 태그가 없을 경우 빈 문자열
        print(console_text)

        # 텍스트 파일로 저장
        with open(output_txt_file, 'w', encoding='utf-8') as file:
            file.write(console_text)

        print(f"<pre> 태그의 텍스트가 {output_txt_file}에 저장되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
input_html_file = "SunSpider 1.0.2 JavaScript Benchmark Results (sunspider-1.0.2 test suite).html"  # HTML 파일 이름
output_txt_file = "output.txt"  # 저장할 텍스트 파일 이름
parse_pre_tag_from_html(input_html_file, output_txt_file)
