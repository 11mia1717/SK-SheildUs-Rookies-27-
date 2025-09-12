from openpyxl import Workbook

wb = Workbook() #워크북생성
ws = wb.active #워크시트에 접근
ws.title = "새 워크시트 타이틀"

#malware-traffic-analysis 수집하여 아래코드를 이용해 엑셀로 저장
#txt파일 저장을 엑셀 팡리 형태로 저장하는 방식
for i in range(10):
    row_cell = ws.cell(row=(i+1), column=1)
    row_cell.value = str(i+1) + " 번째 데이터 저장"


#엑셀 저장(덮어쓰기)
wb.save('text.xlsx')