# AC
https://www.acmicpc.net/problem/5430

### 유형
- 구현
- 데큐

### 풀이
- error를 출력하는 경우는, 큐가 빈 상태에서 D 명령을 했을 때 뿐이다.
- 빈 배열을 출력할 수 있다.
- 이 부분을 인지 못해서 오래 걸렸다.
```java
public class J27_AC {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		
		int CT = Integer.parseInt(br.readLine());
		for (int tc = 0; tc < CT; tc++) {
			
			// 수행할 함수
			String func = br.readLine();
			int N = Integer.parseInt(br.readLine());
			
			String input = br.readLine();
			input = input.substring(1,input.length()-1);
			
			Deque<Integer> DQ = new ArrayDeque<Integer>();
			
			if ( input.length() > 0 ) {
				
				String[] arr = input.split(",");
				for (int i = 0; i < arr.length; i++) {
					DQ.add(Integer.parseInt(arr[i]));
				}
				
			}
			
			boolean reverse = false;
			boolean error = false;
			// 명령 수행
			for (int i = 0; i < func.length(); i++) {
				if ( func.charAt(i) == 'D' ) {
					
					if ( DQ.isEmpty() ) {
						error = true;
						break;
					}
					
					if ( reverse ) {
						// 뒤에서 뺌
						DQ.pollLast();
					} else {
						DQ.pollFirst();
					}
					
				} else {
					reverse = !reverse;
				}
			}
			
			// 출력
			if ( error ) {
				bw.append("error\n");
			} else {
				bw.append("[");
				
				if ( reverse ) {
					while( DQ.size() > 1  ) {
						bw.append(DQ.pollLast()+",");
					}
					if ( !DQ.isEmpty() ) {
						bw.append(DQ.pollLast()+"");
					}
				} else {
					while( DQ.size() > 1 ) {
						bw.append(DQ.pollFirst()+",");
					}
					if ( !DQ.isEmpty() ) {
						bw.append(DQ.pollLast()+"");
					}
				}
				
				bw.append("]\n");
				
			}
			
		}
		bw.flush();
		bw.close();
		
	}

}


```