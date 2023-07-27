'''캐시 :  임시저장소
(필요한 데이터나 자주 사용하는 데이터를 임시로 보관하고 필요시 바로 불러올 수 있음->빠르게 처리가능,
하지만 저장공간이 작은편이라 꽉차면 효율적으로 비워줄 수 있어야함)
LRU알고리즘 : 가장 최근에 사용된 적이 없는 캐시의 메모리부터 대체하며 새로운 데이터로 갱신
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.
1. 캐시크기와 도시이름을 입력받음
2. n칸짜리 list를 만들어서 일단 순서대로 도시이름을 집어넣음
3. 만약 삽입하는 도시이름 중에서 list에 있는 값과 같은게 있으면 answer에 +1을하고 없다면 +5를 함(도시개수만큼 반복)
4. 반복이 끝나면 answer값 출력
'''

def solution(cacheSize, cities):
    answer = 0
    cache = []
    #대소문자 구분이 없으므로 전부 소문자로 변경
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            answer += 5
        else:
            #city가 cache라는 빈 리스트에 이미 존재한다면 +1
            if city in cache:
                answer += 1
                if len(cache) >= cacheSize:
                    cache.remove(city)
                    cache.append(city)
                else:
                    cache.append(city)
            else:
                answer += 5
                if len(cache) >= cacheSize:
                    cache.pop(0) #제일 앞에 있는 도시 pop
                    cache.append(city)
                else:
                    cache.append(city)

    return answer