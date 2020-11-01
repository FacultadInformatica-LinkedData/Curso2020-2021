package model;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileManager;

public class AppModel {
	
	@SuppressWarnings("deprecation")
	public static void main (String [] args) {
		// Read the data and save the graph
		Model model = ModelFactory.createDefaultModel();
		InputStream in = FileManager.get().open("data/data.nt");
		model.read(in, null, "N-TRIPLES");		
		
		
		// Get district names
		System.out.println("District");
		String queryString = "SELECT ?URI ?x {" + 
				"?URI <http://www.semanticweb.org/bicimad/properties#district_name> ?x}";
		
		HashMap<String, String> districts = consultWithSparql(queryString, model);
		printResults(districts);
				
		// Get neighbourhood names
		System.out.println("\n\n\nNeighbourhood");
		String districtURI = "<http://www.semanticweb.org/bicimad/classes/District/Chamberi%20%28Madrid%29>";
		queryString = "SELECT ?URI ?x {" + 
				"?URI <http://www.semanticweb.org/bicimad/properties#has_district> " + districtURI + "." + 
				"?URI <http://www.semanticweb.org/bicimad/properties#neighbourhood_name> ?x}";
		
		HashMap<String, String> neighbourhoods = consultWithSparql(queryString, model);
		printResults(neighbourhoods);
		
		// Get addresses
		System.out.println(" \n\n\nAddresses");
		String neighbourhoodURI = "<http://www.semanticweb.org/bicimad/classes/Neighbourhood/Almagro%20%28Madrid%29>";
		queryString = "SELECT ?URI ?x {" + 
				"?streetURI <http://www.semanticweb.org/bicimad/properties#has_neighbourhood> " + neighbourhoodURI + "." + 
				"?URI <http://www.semanticweb.org/bicimad/properties#has_street> ?streetURI ." + 
				"?URI <http://www.semanticweb.org/bicimad/properties#has_address> ?x}";
		
		HashMap<String, String> addresses = consultWithSparql(queryString, model);
		printResults(addresses);
		
		// Inicializar la vista
		
		
		// Espera de las consultas
		
	}
	
	
	private static HashMap<String, String> consultWithSparql(String queryString, Model model){
		Query query = QueryFactory.create(queryString);
		QueryExecution qexec = QueryExecutionFactory.create(query, model);
		HashMap<String, String> mapResult = new HashMap<String, String>();
			
		QuerySolution result = null;
		try {
		    ResultSet results = qexec.execSelect();
		    while (results.hasNext()){
		    	result = results.next();
		    	mapResult.put(result.get("x").toString(), result.get("URI").toString());
		    }
		} finally {
		    qexec.close();
		}
		return mapResult;
	}
	
	// To check the results before the view
	private static void printResults(HashMap<String, String> toPrint) {
		Iterator<String> results = toPrint.keySet().iterator();
		String aux = "";
		while(results.hasNext()) {
			aux = results.next();
			System.out.println(aux + ": " + toPrint.get(aux));
		}
	}
}
