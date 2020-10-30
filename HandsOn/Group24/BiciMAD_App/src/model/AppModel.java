package model;

import java.beans.Statement;
import java.io.*;

import org.eclipse.rdf4j.query.*;
import org.eclipse.rdf4j.rio.*;

public class AppModel {
	
	public static void main (String [] args) {
		// Read the data and save the graph
		File data = new File("data/data.nt");
		
		// Pueba para ver que el archivo está bien abierto -> cuando sepamos como va la quitamos
		try {
			FileReader fr = new FileReader(data);
			BufferedReader br = new BufferedReader(fr);
			System.out.println(br.readLine());
			br.close();
		} catch (IOException e1) {
			e1.printStackTrace();
			System.out.println("Couldn't read the data");
		}
		
		InputStream isData = null;
		RDFParser rdfParser = null;
		try {
			isData = new FileInputStream(data);	
		} catch (FileNotFoundException e2) {
			System.out.println("Couldn't create the FileInputStream");
			e2.printStackTrace();
	    }
		try {
			// Aqui esta el error, pero ni siquiera cogemos la excepcion
			rdfParser = Rio.createParser(RDFFormat.NTRIPLES);
		} catch (Exception e) {
			System.out.println("Couldn't create the rdfParser");
		}
		
		try {
			rdfParser.parse(isData, "");
		} catch (RDFParseException | RDFHandlerException | IOException e) {
			System.out.println("Couldn't parse the data");
			e.printStackTrace();
		}
		
		// Prueba para imprimir
		try (GraphQueryResult res = QueryResults.parseGraphBackground(isData, "/data/data.nt", RDFFormat.NTRIPLES)) {
			while (res.hasNext()) {
				Statement st = (Statement) res.next();
				System.out.println(st.toString());
			}
		}
		
		// Inicializar la vista
		
		// Espera de las consultas
		
	}
}
