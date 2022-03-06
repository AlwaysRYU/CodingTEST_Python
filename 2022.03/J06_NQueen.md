# N-Queen
https://www.acmicpc.net/problem/9663

### 유형
- 백트래킹

### 풀이
- 또 같은 실수를 했다..
- 아래는 시간초과 코드
- 열단위는 생략하면 된다.
```java
package Y2022D03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class J09_NQueen {

	static int N;
	static int[][] field;
	static int count;
	static int[] dx = { 1, 0, 1 };
	static int[] dy = { 1, 0, 1 };
	static int[] queen;
	
	static BufferedWriter bw;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		N = Integer.parseInt(br.readLine());
		field = new int[N][N];
		queen = new int[N];
		for (int i = 0; i < N; i++) {
			queen[i] = -1;
		}
		count = 0;
		
		for (int i = 0; i < (N*N); i++) {
			int nx = i / N;
			int ny = i % N;
			field[nx][ny] = 1;
			queen[0] = i;
			setchess(1, i);
			queen[0] = -1;
			field[nx][ny] = 0;
		}
		
		System.out.println(count);
		
		
		
	}
	private static void setchess(int number, int index) {
		
		if ( number == N ) {
			count += 1;
			return;
		}
		
		
		
		for (int i = index; i < (N*N); i++) {
			int nx = i / N;
			int ny = i % N;
			
			boolean isok = true;
			
			for (int j = 0; j < number; j++) {
				if ( isok == false ) break;
				
				if ( queen[j] == -1 ) continue;
				else {
					int now = queen[j];
					int xx = now / N;
					int yy = now % N;
					
					int temp = Math.abs(index-i);
					// 가로
					if ( ( xx == nx ) 
							|| ( yy == ny ) 
							||  ( Math.abs( xx - nx) == Math.abs(yy-ny) )
							) {
						// 겹치면
						isok = false;
						break;
					}
					
				}
			}
			
			if ( isok ) {
				field[nx][ny] = 1;
				queen[number] = i;
				setchess(number+1, i);
				queen[number] = -1;
				field[nx][ny] = 0;
			}

			
			
		}
		
		
		
		
		
	}

}
```