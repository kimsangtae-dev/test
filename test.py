def format_percent_lines(input_file, output_file):
    try:
        # Input 파일 읽기
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()

        # '%'가 포함된 줄을 찾고 한 줄씩 저장
        formatted_lines = []
        for line in lines:
            if '%' in line:
                formatted_lines.append(line.strip() + '\n')

        # Output 파일에 저장
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.writelines(formatted_lines)

        print(f"포맷팅된 내용이 {output_file}에 저장되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

# 사용 예시
input_file = "output.txt"  # 입력 파일 이름
output_file = "result.txt"  # 출력 파일 이름
format_percent_lines(input_file, output_file)
