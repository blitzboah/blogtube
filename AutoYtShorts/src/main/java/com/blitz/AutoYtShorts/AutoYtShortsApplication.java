package com.blitz.AutoYtShorts;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.jsoup.nodes.Document;

import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class AutoYtShortsApplication {

	public static void main(String[] args) {

		String filePath = "/home/blitz/blitz/proj/yt-short-automation/AutoYtShorts/links.txt";

		try{

			Path path = Paths.get(filePath);
			List<String> blogLinks = Files.readAllLines(path);
			String url = blogLinks.getFirst();

			Document doc = Jsoup.connect(url).get();

			String title = doc.title();
			Elements paragraphs= doc.select("p");

			StringBuilder blogContent = new StringBuilder();
			blogContent.append(title).append("\n");
			for (Element paragraph : paragraphs){
				blogContent.append(paragraph.text());
			}

			try(FileWriter writer = new FileWriter("/home/blitz/blitz/proj/yt-short-automation/AutoYtShorts/content.txt")){
				writer.write(blogContent.toString());
			}

			System.out.println("done");
			//blogLinks.removeFirst();
			//Files.write(path, blogLinks);

		}
		catch (IOException e){
			System.out.println("error");
			System.out.println(e.getMessage());
		}
	}

}
