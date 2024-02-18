package bronze.camp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_킹_1063 {
	static BufferedWriter bw;
	static BufferedReader br;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));

		st = new StringTokenizer(br.readLine(), " ");
		String kingPosition = st.nextToken();
		String dolPosition = st.nextToken();
		int kingC = kingPosition.charAt(0) - 65;
		int kingR = kingPosition.charAt(1) - 49;
		int dolC = dolPosition.charAt(0) - 65;
		int dolR = dolPosition.charAt(1) - 49;

		int N = Integer.parseInt(st.nextToken());

		int[][] board = new int[8][8];
		int nextR = kingR;
		int nextC = kingC;
		int nextdolR = dolR;
		int nextdolC = dolC;
		for (int i = 0; i < N; i++) {
			String move = br.readLine();
			switch (move) {
			case "R": {
				nextC += 1;
				break;
			}
			case "L": {
				nextC -= 1;
				break;
			}
			case "B": {
				nextR -= 1;
				break;
			}
			case "T": {
				nextR += 1;
				break;
			}
			case "RT": {
				nextR += 1;
				nextC += 1;
				break;

			}
			case "LT": {
				nextR += 1;
				nextC -= 1;
				break;

			}
			case "RB": {
				nextR -= 1;
				nextC += 1;
				break;
			}
			case "LB": {
				nextR -= 1;
				nextC -= 1;
				break;
			}
			}

			// 만약에 킹이랑 돌이랑 만나면
			if (nextR == dolR && nextC == dolC) {
				nextdolC += (nextC - kingC);
				nextdolR += (nextR - kingR);
				if (!(nextdolR >= 0 && nextdolR < 8 && nextdolC >= 0 && nextdolC < 8)) {
					nextdolR = dolR;
					nextdolC = dolC;
					continue;
				}
				dolR = nextdolR;
				dolC = nextdolC;
			}

			if (!(nextR >= 0 && nextR < 8 && nextC >= 0 && nextC < 8)) {
				nextR = kingR;
				nextC = kingC;
				continue;
			}
			kingR = nextR;
			kingC = nextC;
		}
		char A = (char) (kingC + 65);
		char B = (char) (kingR + 49);
		char C = (char) (dolC + 65);
		char D = (char) (dolR + 49);
		System.out.println(A + "" + B);
		System.out.println(C + "" + D);

	}
}
