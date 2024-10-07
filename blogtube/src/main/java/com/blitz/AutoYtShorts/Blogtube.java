package com.blitz.AutoYtShorts;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.nodes.Document;

import java.io.FileWriter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.HashSet;

public class Blogtube {

	public static void main(String[] args) {

		String filePath = "blogtube/links.txt";

		try {

			Path path = Paths.get(filePath);
			List<String> blogLinks = Files.readAllLines(path);
			String url = blogLinks.getFirst();

			Document doc = Jsoup.connect(url).get();

			Elements paragraphs = doc.select("p, td");

			//hashset for avoiding duplication
			HashSet<String> seenText = new HashSet<>();
			StringBuilder blogContent = new StringBuilder();

			for (Element paragraph : paragraphs) {
				String text = paragraph.text();
				if (!seenText.contains(text) && !text.trim().isEmpty()) {
					blogContent.append(text).append("\n");
					seenText.add(text);
				}
			}

			try (FileWriter writer = new FileWriter("blogtube/content.txt")) {
				writer.write(blogContent.toString());
			}

			System.out.println("done");
		} catch (Exception e) {
			System.out.println("error");
			System.out.println(e.getMessage());
		}
	}
}
