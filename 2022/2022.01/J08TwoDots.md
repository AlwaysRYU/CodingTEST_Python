# Two Dots
https://www.acmicpc.net/problem/16929

### 유형
- 재귀
- 조건에 맞는 것 찾기

### 풀이
- DFS를 이용해서 풀었다.
- 괜히 복잡하게 생각해서 코드가 좀 더러워진 느낌.
```java
package Y2022D01;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class D08TwoDots {
	
	static char now;
	static boolean find;
	static int N,M;
	static char[][] field;
	static boolean[][] visit;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = {  0, 1, 0,-1 };
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		field = new char[N][M];
		visit = new boolean[N][M];
		
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				char temp = str.charAt(j);
				field[i][j] = temp;
			}
		}
		
		find = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if ( visit[i][j] == false ) {
					visit[i][j] = true;
					now = field[i][j];

					for (int k = 0; k < 4; k++) {
						int nx = i + dx[k];
						int ny = j + dy[k];
						if ( nx >= 0 && nx < N && ny >= 0 && ny < M
								&& field[nx][ny] == now && visit[nx][ny] == false ) {
							visit[nx][ny] = true;
							dfs(nx,ny,i,j, 2);
							visit[nx][ny] = false;
						}
					}

				}
				
				if (find) break;
			}
			if (find) break;
		}
		
		
		if (find) System.out.println("Yes");
		else System.out.println("No");
		
		
		
		
		
		
	}

	private static void dfs(int i, int j, int XX, int YY, int count) {
		// TODO Auto-generated method stub
		for (int k = 0; k < 4; k++) {
			int nx = i + dx[k];
			int ny = j + dy[k];
			
			if ( nx == XX && ny == YY && count >= 4 ) {
				// 조건에 만족하면
				visit[nx][ny] = true;
				find = true;
				return;
				
			} else if ( nx >= 0 && nx < N && ny >= 0 && ny < M
					&& field[nx][ny] == now && visit[nx][ny] == false ) {
				// 갈수 있으면
				visit[nx][ny] = true;
				dfs(nx,ny,XX,YY, count+1);
				visit[nx][ny] = false;
			}
			
		}
		
		
	}

}

```

### 내가 찝집해서 찾아본 더 간단한 풀이
- 같이 dfs를 쓰지만 더 간단한 방식
- 맞다. 사실 크게 어려운 문제는 아니다.
```java
public class Main {

    static char[][] a;
    static boolean[][] visited;
    final static int dy[] = new int[]{1, -1, 0, 0};
    final static int dx[] = new int[]{0, 0, 1, -1};
    static int n, m;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        a = new char[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; ++i) {
            a[i] = sc.next().toCharArray();
        }
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j) {

                if (visited[i][j] ==  false) {
                    boolean cand = dfs(i,j,-1,-1,a[i][j]);
                    if(cand) {
                    System.out.println("Yes");
                        System.exit(0);
                    }
                }
            }
        System.out.println("No");
    }

    static boolean dfs(int y, int x, int by, int bx, char alp) {

        if (visited[y][x]) return true;

        visited[y][x] = true;

        for (int k = 0; k < 4; ++k) {
            int ny = y + dy[k];
            int nx = x + dx[k];
            if (!(0 <= ny && ny < n && 0 <= nx && nx < m)) continue;
            if (a[ny][nx] != alp) continue;
            if (ny == by && nx == bx) continue;

            if(dfs(ny, nx, y, x, alp))
                return true;
        }
        return false;
    }
}
```