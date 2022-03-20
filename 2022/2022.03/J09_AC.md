# AC
https://www.acmicpc.net/problem/5430

### 유형
- 구현
- 데큐

### 풀이
- 자바에도 deque 를 사용할 수 있는지 몰랐다.
- 그래서 arraylist로 구현했는데, 시간초과가 난다.
- 이것을 제외하면 풀이에서 차이는 없다. 자료구조의 중요성
```java
package Y2022D03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class J12_AC {
	
	static BufferedWriter bw;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int Test = Integer.parseInt(br.readLine());
		for (int ttt = 0; ttt < Test; ttt++) {
			String order = br.readLine();
			int N = Integer.parseInt(br.readLine());
			
			ArrayList<Integer> list = new ArrayList<>(); 
			boolean reverse = false;
			
			String[] number = br.readLine().split(",");
			for (int i = 0; i < N; i++) {
				if ( i == 0 ) {
					list.add(number[i].charAt(1) - '0' );
				} else {
					list.add( number[i].charAt(0) - '0' );
				}
			}
			
			boolean error = false;
			for (int i = 0; i < order.length(); i++) {
				char X = order.charAt(i);
				if ( X == 'R' ) {
					reverse = !reverse;
				} else {
					if ( list.size() == 0 ) {
						error = true;
						break;
					}
					
					if ( reverse ) {
						list.remove(list.size() -1 );
					} else {
						list.remove(0);
					}
				}
			}
			
			String answer = "";
			if ( error ) {
				bw.append("error\n");
			} else if ( reverse ) {
				answer = "[";
				for (int i = list.size()-1 ; i >= 0 ; i-- ) {
					answer += list.get(i);
					if ( i == 0 )break;
					answer += ",";
				}
				answer += "]\n";
				
			} else {
				answer = "[";
				for (int j = 0; j < list.size(); j++) {
					answer += list.get(j);
					if ( j == list.size()-1 )break;
					answer += ",";
				}
				answer += "]\n";
			}
			
			bw.append(answer);
			
		}
		
		
		bw.flush();
		bw.close();
		br.close();
		
	}

}

```

### 풀이2
- deque를 사용한 정답 코드
- https://st-lab.tistory.com/221
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayDeque;
 
public class Main {
 
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
 
		
		ArrayDeque<Integer> deque;
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		
		
		
		while(T --> 0) {
			
			String command = br.readLine();	// 문제에서 p에 해당하는 명령어
			int n = Integer.parseInt(br.readLine());
			
			st = new StringTokenizer(br.readLine(), "[],");
			
			deque = new ArrayDeque<Integer>();
			
			// 덱에 배열 원소를 넣어준다.
			for(int i = 0; i < n; i++) {
				deque.add(Integer.parseInt(st.nextToken()));
			}
			
			AC(command, deque);
		}
		
		System.out.println(sb);
		
	}
	
	public static void AC(String command, ArrayDeque<Integer> deque) {
		
		boolean isRight = true;
		
		for(char cmd : command.toCharArray()) {
			
			if(cmd == 'R') {
				isRight = !isRight;	// 방향을 바꿔준다.
				continue;
			}
			
			
			// 아래는 D의 경우
			
			// D 함수이면서 isRight가 true 일 경우
			if(isRight) {
				
				// 만약 반환 된 원소가 없을 경우 error를 출력하도록 하고 함수 종료
				if(deque.pollFirst() == null) {
					sb.append("error\n");
					return;
				}
				
			}
			else {
				// 만약 반환 된 원소가 없을 경우 error를 출력하도록 하고 함수 종료
				if(deque.pollLast() == null) {
					sb.append("error\n");
					return;
				}	
			}
		}
		
		// 모든 함수들이 정상적으로 작동했다면 덱의 남은 요소들을 출력문으로 만들어준다.
		makePrintString(deque, isRight);
		
	}
	
	public static void makePrintString(ArrayDeque<Integer> deque, boolean isRight) {
		
		sb.append('[');	// 여는 대괄호 먼저 StringBuilder에 저장
		
		if(deque.size() > 0) {	//만약 출력 할 원소가 한 개 이상일 경우
			
			if(isRight) {	// 정방향일경우 
				
				sb.append(deque.pollFirst());	// 먼저 첫 번째 원소를 넘겨준다.
				
				// 그 다음 원소부터 반점을 먼저 넘겨준 후 덱의 원소를 하나씩 뽑아 넘긴다. 
				while(!deque.isEmpty()) {
					sb.append(',').append(deque.pollFirst());
				}
			}
			else {	// 역방향일경우 
				sb.append(deque.pollLast());	// 먼저 뒤에서부터 첫 번째 원소를 넘겨준다.
				
				// 그 다음 원소부터 반점을 먼저 넘겨준 후 덱의 원소를 뒤에서부터 하나씩 뽑아 넘긴다. 
				while(!deque.isEmpty()) {
					sb.append(',').append(deque.pollLast());
				}
			}
		}
		
		sb.append(']').append('\n');	// 닫는 대괄호 및 개행으로 마무리
	}
}
```