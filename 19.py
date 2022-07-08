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

#Key,Value 쌍 얻기(items)
a.items()
#Key,Value 쌍 모두 지우기(clear)
a.clear()
a
#Key로 Value 얻기(get)
a = {'name' : jjj, 'phone' : '01012345678', 'birth' : '0111'}
a.get('name')
a.get('phone')

#딕셔너리에서 찾는 값이 없을 경우 미리 정해 둔 디폴트값을 대신 가져오고 싶을 때: get(x, '디폴트값')
a.get('foo', 'bar')

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name' : jjj, 'phone' : '01012345678', 'birth' : '0111'}
'name' in a
'email' in a
