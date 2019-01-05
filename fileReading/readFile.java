import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Launcher {

	public static void main(String[] args) {
		File file = new File("src/package/file.txt");
		readFile(file);
	}
	
	private static void readFile(File file) {
		BufferedReader bufferedReader = null;
		String line;

		try {
			bufferedReader = new BufferedReader(new FileReader(file));
		} catch (FileNotFoundException e) {
			System.out.println("Error opening file: " + file.toString());
			System.exit(0);
		}
		
		try {
			while ((line = bufferedReader.readLine()) != null) {
				System.out.println(line);
			}	
		} catch (IOException e) {
			System.out.println("Error reading file " + file.toString());
      System.exit(0);
		}
	}

}
