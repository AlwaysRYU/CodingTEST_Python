# Binary Tree Nodes
https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

# 문제
- 노드의 종류를 구분하는 SQL 문제.
- N과 P라는 두 개의 열이 포함된 테이블 BST가 제공
- N은 이진 트리의 노드 값을 나타내고 P는 N의 부모입니다.
- 노드의 값으로 정렬된 Binary Tree의 노드 유형을 찾는 쿼리를 작성한다.
- 각 노드에 대해 다음 중 하나를 출력

루트: 노드가 루트 노드인 경우.
리프: 노드가 리프 노드인 경우.
내부: 노드가 루트 노드도 리프 노드도 아닌 경우.

# 풀이
- 서브쿼리
SELECT N, CASE WHEN P IS NULL THEN 'Root'
               WHEN N NOT IN ( SELECT DISTINCT P 
                                FROM BST
                                WHERE P IS NOT NULL ) THEN 'Leaf'
                ELSE 'Inner'
                END
FROM BST
ORDER BY N;
-- N 을 출력
-- P 가 null 이면 루트노드
-- N 이 P 리스트 안에 들어가지 않은 친구들은 Leaf
-- 그 어느쪽도 아니면 Inner


# 풀이
- 조인
- N이 P 와같다면 
SELECT DISTINCT A.N, CASE WHEN A.P IS NULL THEN 'Root'
                          WHEN B.P IS NULL THEN 'Leaf'
                          ELSE 'Inner'
                          END
FROM BST A LEFT JOIN BST B ON A.N = B.P
ORDER BY A.N;