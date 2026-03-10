# 시작횟수
i = 1
# 총 통과항목수
success = 0
# 미통과항목 저장
fail = []

while True:
    # input 입력
    if i == 1:
        check = input(f"[{i}/5] DB 마이그레이션 완료 여부 (Y/N): ").upper()
    elif i == 2:
        check = input(f"[{i}/5]  application-prod.properties 설정 확인(Y/N): ").upper()
    elif i == 3:
        check = input(f"[{i}/5]  JWT Secret Key 변경 여부 (Y/N): ").upper()
    elif i == 4:
        check = input(f"[{i}/5] CORS 허용 도메인 설정 완료 (Y/N): ").upper()
    elif i == 5:
        check = input(f"[{i}/5] API 엔드포인트 테스트 통과 (Y/N): ").upper()
    else:
        break

    # 완료/미완료 처리
    if check == "Y":
        print("→ 완료")
        # 총 통과항목수 누적
        success += 1
    elif check == "N":
        print("→ 미완료")
        # fail.push(i)
    else:
        print("→ Y or N으로 재입력 요망")
        continue

    # 횟수누적
    i += 1

if success == 5:
    print("배포 승인! 배포를 진행하세요.")
else:
    print(f"배포 보류! {5-success}개 항목을 해결 후 재시도하세요.'")
    print(fail)
