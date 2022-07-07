#KEY에는 리스트를 쓸 수 없다
a = {[1,2] : 'hi'} #리스트를 key로 사용
#형 오류 발생

#딕셔너리 관련 함수 
#KEY 리스트 만들기(keys)
a = {'name' : 'pey', 'phone' : '01012345678', 'birth' : '1118'}
dict_keys(['name', 'phone', 'birth'])
a.keys() #딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다

#3.0이후 버전일 경우 반환 값으로 리스트가 필요한 경우 'list(a.keys())' 사용

#dict_keys 객체를 리스트로 변환하면
list(a.keys())

#Value 리스트 만들기 (values)
a.values()
