package main;

import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;

public class App {


	//static String tipo = "Restos";
	//static String distrito = "Centro";

	public static void main(String[] args) {
		
		//sparqlTest(tipo, distrito);

	}

	static String sparqlTest(String tipo, String distrito) {
		//FileManager.get().addLocatorClassLoader(App.class.getClassLoader());
		//Model model = FileManager.get().loadModel("c:/users/Mery Sánchez/eclipse-workspace/HandsOn-Group06/src/output.nt");
		
		String resultado = "\n";
		
		Model model;

		model = ModelFactory.createDefaultModel();
		model.read("output.nt");

		// Para "traducir" valores y que los busque bien
		switch (tipo) {
		case "Restos":
			tipo = "RESTO";
			break;
		case "Vidrio":
			tipo = "VIDRIO";
			break;
		case "Envases":
			tipo = "ENVASES";
			break;
		case "Orgánica":
			tipo = "ORGANICA";
			break;
		case "Papel - Cartón":
			tipo = "PAPEL-CARTON";
			break;
		default:
					
		}
		
		switch (distrito) {
		case "Chamberí":
			distrito = "Chamber%C3%AD";
			break;
		case "Ciudad Lineal":
			distrito = "Ciudad%20Lineal";
			break;
		case "Fuencarral - El Pardo":
			distrito = "Fuencarral-El%20Pardo";
			break;
		case "Moncloa - Aravaca":
			distrito = "Moncloa-Aravaca";
			break;
		case "Tetuán":
			distrito = "Tetu%C3%A1n";
			break;
		default:
				
		}
		
		String querystr =
				// "SELECT * WHERE { ?s ?p ?o } LIMIT 100";

				"SELECT ?direccion WHERE { " +
			    "?s <http://contenedoresdemadrid.com/Properties#locatedDistrict> <http://contenedoresdemadrid.com/Classes/District/" + distrito + ">. " +
			    "?s <http://contenedoresdemadrid.com/Properties#typeResidue> <http://contenedoresdemadrid.com/Classes/TypeResidue/" + tipo + ">. " + 
			    "?s <http://contenedoresdemadrid.com/Properties#hasAddress> ?direccion. }";

		Query query = QueryFactory.create(querystr);
		QueryExecution qexec = QueryExecutionFactory.create(query, model);
		
		try {
			ResultSet results = qexec.execSelect();

			while (results.hasNext()) {
				QuerySolution soln = results.nextSolution();
				//Literal name = soln.getLiteral("direccion");

				
				String a = soln.toString().substring(64, soln.toString().length()-3); //Para limpiarlo porque getLiteral peta
				String b = a.replace(".%20", ", ");
				String c = b.replace("%20", " ");
				String d = c.replace("%C2%A0", " ");
				String e = d.replace("%C3%91", "Ñ");
								
				resultado = resultado + "- " + e + "\n";

			}

		} finally {
			qexec.close();
		}

		if (resultado.equals("\n"))
			resultado = "\n" + "No hay contenedores en la base de datos" + "\n" + "para los campos introducidos";
		
		//System.out.println(resultado);
		
		return resultado;
	}
}
