# Fly me to the Alpha Centuri

### 유형
https://www.acmicpc.net/problem/1011

### 풀이
- 규칙을 찾았지만, 더 수학적으로 구현해야 했다.
```java
public class fly {
	
	static BufferedWriter bw;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		int tc = Integer.parseInt(br.readLine());
		for (int xx = 0; xx < tc; xx++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			
			int distance = B - A;
			
			int max = (int)Math.sqrt(distance);	// 소수점 버림
            
			if(max == Math.sqrt(distance)) {
				System.out.println(max * 2 - 1);
			}
			else if(distance <= max * max + max) {
				System.out.println(max * 2);
			}
			else {
				System.out.println(max * 2 + 1);
			}
			
			
		}
	}
}
```

### 풀이 2
- 사이즈가 초과 오류
```java

public class fly {
	static BufferedWriter bw;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
//		double x = 2_147_483_648;
		int[] arr = new int[2_147_483_647];
		
		// 3이상
		// 
		int count = 2;
		int gop = 0;
		int index = 0;
		int value = 3;
		while ( index < 2_147_483_647 ) {
			
			for (int k = 0; k < 2; k++) {
				for (int i = 0; i < count; i++) {
					arr[index] = value;
					index += 1;
					if ( index == 2_147_483_647 ) break;
				}
				if ( index == 2_147_483_647 ) break;
				
				value += 1;
				count += 1;

				if ( index == 2_147_483_647 ) break;
			}
			
		}
		
//		System.out.println(x);
	}

	

}
```