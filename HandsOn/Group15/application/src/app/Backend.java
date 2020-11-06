package app;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;

import java.net.URLDecoder;
import java.util.ArrayList;

public class Backend {

	Model model = ModelFactory.createDefaultModel();
	
	public Backend() {}
	
	public ArrayList<String> getMunicipality() { 
		
		ArrayList<String> municipios = new ArrayList<String>();
		String centro;
		
		model.read("resources/output.nt");
		
		String q1 = "PREFIX properties: <http://linkeddata.es/group15/ontology/studyCentersMadrid/properties#> \r\n"
				+ "  PREFIX classes: <http://linkeddata.es/group15/ontology/studyCentersMadrid/classes#> \r\n"
				+ "  PREFIX individuals: <http://linkeddata.es/group15/ontology/studyCentersMadrid/individuals/municipalities/>\r\n"
				+ "\r\n" + "  SELECT DISTINCT ?municipio \r\n" + "  WHERE { \r\n"
				+ "    ?municipio a classes:Municipality\r\n}";

		Query query1 = QueryFactory.create(q1);
		QueryExecution query1exec = QueryExecutionFactory.create(query1, model);
		ResultSet results = query1exec.execSelect();

		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			centro = soln.get("municipio").toString();
			municipios.add(decodedFun(centro));			
		}
		return municipios;
	}

	public ArrayList<String> execQuery(String lista[]) {

		ArrayList<String> centros = new ArrayList<String>();
		String centro;
		model.read("resources/output.nt");

		String q1 = "PREFIX properties: <http://linkeddata.es/group15/ontology/studyCentersMadrid/properties#> \r\n"
				+ "  PREFIX classes: <http://linkeddata.es/group15/ontology/studyCentersMadrid/classes#> \r\n"
				+ "  PREFIX individuals: <http://linkeddata.es/group15/ontology/studyCentersMadrid/individuals/municipalities/>\r\n"
				+ "  PREFIX owl: <http://www.w3.org/2002/07/owl#> \r\n"
				+ "\r\n" + "  SELECT DISTINCT ?centrosNombre ?link \r\n" + "  WHERE { \r\n"
				+ "    ?centros properties:located individuals:" + lista[0] + " .\r\n"
				+ "	   ?centros properties:titularity " + lista[1] + " .\r\n"
				+ "    ?centros  properties:centerName ?centrosNombre .\r\n"
				+ "	   individuals:" + lista[0] + " owl:sameAs ?link\r\n}";
		
		String q2 = "PREFIX properties: <http://linkeddata.es/group15/ontology/studyCentersMadrid/properties#> \r\n"
				+ "  PREFIX classes: <http://linkeddata.es/group15/ontology/studyCentersMadrid/classes#> \r\n"
				+ "  PREFIX individuals: <http://linkeddata.es/group15/ontology/studyCentersMadrid/individuals/municipalities/>\r\n"
				+ "  PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n"
				+ "\r\n" + "  SELECT DISTINCT ?centrosNombre \r\n" + "  WHERE { \r\n"
				+ "    ?centros properties:located individuals:" + lista[0] + " .\r\n"
				//+ "    ?centros properties:titularity \"PRIVADO\"^^string .\r\n"
				+ "    ?centros  properties:centerName ?centrosNombre .\r\n"
				+ "    ?municipio  a classes:Municipality\r\n}";

		Query query1 = QueryFactory.create(q2);

		QueryExecution query1exec = QueryExecutionFactory.create(query1, model);

		ResultSet results = query1exec.execSelect();

		if (!results.hasNext())
			System.out.println("No se ha encontrado ningun centro");

		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			centro = soln.get("centrosNombre").toString();
			centros.add(decodedFun(centro));			
		}
		return centros;
	}
	
	private String decodedFun(String centro) {
		String result="Error";
		try {
			result = URLDecoder.decode(centro, "UTF-8");
			result = result.substring(result.lastIndexOf('/') + 1);
			System.out.println(result);			
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
	}
}