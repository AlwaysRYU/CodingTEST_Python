# N-Queen
https://www.acmicpc.net/problem/9663

### 유형
- 최적합 찾기
- 브루트 포스

### 풀이
- 항상 배열관련해서는 반복될 경우 수학적으로 생각하는 습관을 기르자.
- 이건 수학적으로 생각하지 않은 결과
- 시간초과 발생
```java
package Y2022D01;

import java.io.BufferedReader;
import java.io.InputStreamReader;

//https://www.acmicpc.net/problem/9663
public class D24_NQueen {
	
	
	static int N, answer = 0;
	static int[][] field;
	static int[] dx = { -1, -1, -1, 0, 0, 1, 1, 1};
	static int[] dy = { -1,  0,  1,-1, 1,-1, 0, 1};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 초기화
		N = Integer.parseInt(br.readLine());
		field = new int[N][N];
		
		Queen(0, 0);
		System.out.println(answer);
		
		
	}
	
	private static void Queen(int position, int depth) {
		// TODO Auto-generated method stub
		if ( depth == N ) {
			answer += 1;
			return;
		}
		
		for (int i = position; i < N*N; i++) {
			int x = i/N;
			int y = i%N;
			if ( field[x][y] == 0 ) {
				
				boolean isOK = true;
				for (int k = 0; k < 8; k++) {
					
					int nx = x + dx[k];
					int ny = y + dy[k];
					while( nx >=0 && nx < N && ny >= 0 && ny < N ) {
						if ( field[nx][ny] == 1) {
							isOK = false;
							break;
						}
						nx += dx[k];
						ny += dy[k];
						
					}
					if ( isOK == false ) break;
				}
				
				if ( isOK == true ) {
					// 배치 후 넘기기  
					field[x][y] = 1;
					Queen( x*N, depth+1);
					field[x][y] = 0;
				}
			}
		}
		
		
	}

}

```

### 풀이 2
- 열번호만 기록 해두기
- 실제 퀸이 놓이는 위치는 관심 없으니 열만 기록하여서 계산하기
```java
package Y2022D01;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

//https://www.acmicpc.net/problem/9663
public class D24_NQueen2 {

	static int N, answer = 0;
	static int[] choice;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 초기화
		N = Integer.parseInt(br.readLine());
		choice = new int[N];
		Queen(0);
		System.out.println(answer);
	}

	private static void Queen(int depth) {
		// TODO Auto-generated method stub
		if (depth == N) {
			answer += 1;
			return;
		}

		for (int i = 0; i < N; i++) {
			choice[depth] = i;
			if (Possibility(depth)) {
				Queen(depth + 1);
			}
		}

	}

	private static boolean Possibility(int col) {
		for (int i = 0; i < col; i++) {
			if (choice[col] == choice[i]) return false;
			else if (Math.abs(col - i) == Math.abs(choice[col] - choice[i])) return false;
		}
		
		return true;
	}

}

```