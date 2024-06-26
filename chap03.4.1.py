import seaborn as sns

#예제로 seaborn 패키지의 타이타닉 데이터셋을 불러온 후
df=sns.load_dataset('titanic')

#맨위 살펴보기(5줄)
print(df.head())
print()
print()

#맨 아래 살펴보기(5줄)
print(df.tail())
print()
print()

#데이터 프레임의 크기를 확인할 때
print(df.shape)
print()
print()

#데이터 프레임의 기본 정보
print(df.info())
print()
print()

#각 열의 고유값 개수를 구할 때는 value_counts() 사용
#sex(성별)의 고유값의 종류와 개수를 확인해 보자
print(df['sex'].value_counts())
print()
print()

#male/0/사망, male/1/생존, female/0/사망, female/1/생존
print(df[['sex', 'survived']].value_counts())
print()
print()

#value.counts(normalize=True) 은 비중으로 계산
#sort_index() 는 인덱스를 정렬해 줌
print(df[['sex', 'survived']].value_counts(normalize=True).sort_index())
print()
print()

#mean() 메서드로 산술 평균을 구할 수 있다.
print(df['survived'].mean())
print()
print()
print(df[['survived', 'age']].mean())
print()
print()


#min() 은 최소값, max() 는 최대값, #median() 는 중위수
print(df['fare'].min())
print()
print()

print(df['fare'].max())
print()
print()

print(df['fare'].mean())
print()
print()

print(df['fare'].median())
