package app;


import java.util.ArrayList;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.query.ResultSetFormatter;
import org.apache.jena.rdf.model.Literal;


public class Queries {
	private ArrayList<String> calles;
	private ArrayList<String> distritos;
	private ArrayList<String> conectores;

	public Queries() {
		getValores();
	}

	public ArrayList<String> getCalles(){
		return calles;
	}

	public ArrayList<String> getDistritos(){
		return distritos;
	}

	public ArrayList<String> getConectores(){
		return conectores;
	}

	private void getValores() {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "SELECT DISTINCT ?distrito\r\n"
						+ "WHERE{\r\n"
						+ "    ?s <http://www.eletricrechargemadrid.com/distrito> ?distrito\r\n"
						+ " }");
		ResultSet distrito = qe.execSelect();

		qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "SELECT DISTINCT ?calles \r\n"
						+ "WHERE{\r\n"
						+ "    ?s <http://www.eletricrechargemadrid.com/calle> ?calles\r\n"
						+ " }");
		ResultSet calle = qe.execSelect();

		qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "SELECT DISTINCT ?conectores \r\n"
						+ "WHERE{\r\n"
						+ "    ?s <http://www.eletricrechargemadrid.com/conectores> ?conectores\r\n"
						+ " }");
		ResultSet conector = qe.execSelect();
		distritos = toList(distrito, "distrito");
		calles = toList(calle, "calles");
		conectores = toList(conector,"conectores");
		qe.close();
	}

	public ArrayList<String> toList(ResultSet result, String column) {
		ArrayList<String> aux = new ArrayList<>();
		QuerySolution next = result.next();
		boolean first=true;
		Literal columna;
		if (next!=null) {
			do {
				if(!first) next = result.next();
				String calle = next.getLiteral(column).getString();
				aux.add(calle);
				first = false;
			}while(result.hasNext());
		}
		return aux;
	}

	public ArrayList<PuntoRecarga> toList(ResultSet result) {
		try {
			ArrayList<PuntoRecarga> aux = new ArrayList<>();
			QuerySolution next = result.next();
			boolean first=true;
			Literal conector;
			Literal potencia;
			Literal terminales;
			Literal edificio;
			if (next!=null) {
				do{
					if(!first)
						next = result.next();
					PuntoRecarga pRecarga = new PuntoRecarga();
					pRecarga.setCalle(next.getLiteral("calle").getString());
					conector=next.getLiteral("conector");
					if(conector!=null)
						pRecarga.setConector(next.getLiteral("conector").getString());
					else 
						pRecarga.setConector(" ");
					pRecarga.setCoordX(next.getLiteral("coordX").getString());
					pRecarga.setCoordY(next.getLiteral("coordY").getString());
					pRecarga.setDistrito(next.getLiteral("distrito").getString());
					edificio=next.getLiteral("edificio");
					if(edificio!=null)
						pRecarga.setEdificio(next.getLiteral("edificio").getString());
					else
						pRecarga.setEdificio(" ");
					potencia=next.getLiteral("potencia");
					if(potencia!=null)
						pRecarga.setPotencia(next.getLiteral("potencia").getString());
					else
						pRecarga.setPotencia(" ");
					terminales=next.getLiteral("t");
					if(terminales!=null)
						pRecarga.setTerminal(next.getLiteral("t").getString());
					else
						pRecarga.setTerminal(" ");
					aux.add(pRecarga);
					first=false;
				}while(result.hasNext());
			}
			
			return aux;
		}
		catch(Exception e) {
			return null;
		}
	}

	public ArrayList<PuntoRecarga> busquedaConector(String filtro) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n" + 
						"SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY) \r\n" +
						"WHERE {\r\n" + 
						"  ?puntoRecarga <http://www.eletricrechargemadrid.com/conectores> \""+ filtro +"\" .\r\n" + 
						"  OPTIONAL{?puntoRecarga <http://www.eletricrechargemadrid.com/conectores> ?conector .}\r\n" +
						"  ?puntoRecarga <http://www.eletricrechargemadrid.com/localizacion> ?ubicacion .\r\n" + 
						"  OPTIONAL{?puntoRecarga <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n" +
						"  OPTIONAL{?puntoRecarga <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n" +
						"  ?ubicacion <http://www.eletricrechargemadrid.com/calle> ?calle .\r\n" + 
						"  OPTIONAL{?puntoRecarga <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n" + 
						"  ?ubicacion <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n" + 
						"  ?ubicacion <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY .\r\n" + 
						"  ?puntoRecarga <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n" + 
						"  ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito\r\n" + 
				"} ");
		ResultSet results = qe.execSelect();
		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}


	public ArrayList<PuntoRecarga> busquedaCalle(String filtro) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n"
						+ "SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY) \r\n"
						+ "WHERE {\r\n"
						+ "  ?u <http://www.eletricrechargemadrid.com/calle> \""+ filtro + "\" .\r\n"
						+ "  ?u <http://www.eletricrechargemadrid.com/calle> ?calle .\r\n"
						+ "  ?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n"
						+ "  OPTIONAL{?p <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n"
						+ "	 OPTIONAL{?p <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n"
						+ "	 OPTIONAL{?p <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n"
						+ "  OPTIONAL{?p <http://www.eletricrechargemadrid.com/conectores> ?conector .}\r\n"
						+ "  ?u <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n"
						+ "  ?u <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY .\r\n"
						+ "  ?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n"
						+ "  ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito\r\n"
						+ "}");
		ResultSet results = qe.execSelect();
		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}


	public ArrayList<PuntoRecarga> busquedaDistrito(String filtro) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n"
						+ "SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY) \r\n"
						+ "WHERE {\r\n"
						+ "   	    ?d <http://www.eletricrechargemadrid.com/distrito> \""+ filtro +"\" .\r\n"
						+ "   	    ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito .\r\n"
						+ "			?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n"
						+ "  		OPTIONAL{?p <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n"
						+ "			OPTIONAL{?p <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n"
						+ "			OPTIONAL{?p <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n"
						+ "  		OPTIONAL{?p <http://www.eletricrechargemadrid.com/conectores> ?conector .}\r\n"
						+ "  		?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n"
						+ "  		?u <http://www.eletricrechargemadrid.com/calle>  ?calle .\r\n"
						+ "  		?u <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n"
						+ "  		?u <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY\r\n"
						+ "	} ");
		ResultSet results = qe.execSelect();
		//ResultSetFormatter.out(System.out, results);
		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}


	public ArrayList<PuntoRecarga> busquedaDistritoConector(String distrito, String conector) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n"
						+ "SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY) \r\n"
						+ "WHERE {\r\n"
						+ "   	     ?d <http://www.eletricrechargemadrid.com/distrito> \""+ distrito + "\" .\r\n"
						+ "   	     ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n"
						+ "   	     ?p <http://www.eletricrechargemadrid.com/conectores> \"" + conector + "\" .\r\n"
						+ "  		OPTIONAL{?p <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n"
						+ "			OPTIONAL{?p <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n"
						+ "			OPTIONAL{?p <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n"
						+ "  		OPTIONAL{?p <http://www.eletricrechargemadrid.com/conectores> ?conector .}\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/calle> ?calle .\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY\r\n"
						+ "    }");
		ResultSet results = qe.execSelect();
		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}


	public ArrayList<PuntoRecarga> busquedaCalleConector(String calle, String conector) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n"
						+ "SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY) \r\n"
						+ "WHERE {\r\n"
						+ "       	 ?u <http://www.eletricrechargemadrid.com/calle> \"" + calle + "\" .\r\n"
						+ "       	 ?u <http://www.eletricrechargemadrid.com/calle> ?calle .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/conectores> \"" + conector + "\" .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/conectores> ?conector .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n"
						+ "			 OPTIONAL{?p <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n"
						+ "			 OPTIONAL{?p <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n"
						+ "          ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito .\r\n"
						+ "          OPTIONAL{?p <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY      \r\n"
						+ "    }");
		ResultSet results = qe.execSelect();
		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}
	
	public ArrayList<PuntoRecarga> busquedaDistritoCalleConector(String distrito, String calle, String conector) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\r\n" + 
						"SELECT DISTINCT ?distrito ?calle ?conector ?edificio (xsd:string(?terminales) AS ?t) ?potencia (xsd:string(?CoordenadaX) AS ?coordX) (xsd:string(?CoordenadaY) AS ?coordY)\r\n" + 
						"WHERE {\r\n" + 
						"          ?u <http://www.eletricrechargemadrid.com/calle> \"" + calle + "\" .\r\n" + 
						"          ?u <http://www.eletricrechargemadrid.com/calle> ?calle .\r\n" + 
						"          ?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n" + 
						"          ?p <http://www.eletricrechargemadrid.com/conectores> \"" + conector + "\" .\r\n" + 
						"            ?d <http://www.eletricrechargemadrid.com/distrito> ?\"" + distrito +  "\" .\r\n" + 
						"          ?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n" + 
						"            ?p <http://www.eletricrechargemadrid.com/conectores> ?conector .\r\n" + 
						"          OPTIONAL{?p <http://www.eletricrechargemadrid.com/edificio> ?edificio .}\r\n" + 
						"          OPTIONAL{?p <http://www.eletricrechargemadrid.com/terminales> ?terminales .}\r\n" + 
						"          ?d <http://www.eletricrechargemadrid.com/distrito> ?distrito .\r\n" + 
						"          OPTIONAL{?p <http://www.eletricrechargemadrid.com/potencia> ?potencia .}\r\n" + 
						"          ?u <http://www.eletricrechargemadrid.com/coordenada_x> ?CoordenadaX .\r\n" + 
						"          ?u <http://www.eletricrechargemadrid.com/coordenada_y> ?CoordenadaY      \r\n" + 
						"    }");
		ResultSet results = qe.execSelect();
//		ResultSetFormatter.out(System.out, results);

		ArrayList<PuntoRecarga> aux = toList(results);
		qe.close();
		return aux;
	}
	


	public ArrayList<String> calles(String distrito) {
		QueryExecution qe = QueryExecutionFactory.sparqlService(
				"http://localhost:3030/PuntoRecargaNuevo/query", "SELECT DISTINCT ?calles\r\n"
						+ "WHERE {\r\n"
						+ "        ?d <http://www.eletricrechargemadrid.com/distrito> \"" + distrito + "\" .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/relacion> ?d .\r\n"
						+ "          ?p <http://www.eletricrechargemadrid.com/localizacion> ?u .\r\n"
						+ "          ?u <http://www.eletricrechargemadrid.com/calle> ?calles\r\n"
						+ "    }");
		ResultSet results = qe.execSelect();
		ArrayList<String> aux = toList(results, "calles");
		qe.close();
		return aux;
	}
}
