package modelo;

import java.util.ArrayList;
import java.util.Arrays;

import org.apache.commons.lang3.ArrayUtils;
import org.apache.jena.query.ParameterizedSparqlString;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.RDFNode;

import controlador.Controller;
import gui.Searcher;

public class Engine {

	/* NOTE
	 * 
	 * We tried to do federated queries against Wikidata but our Fuseki's endpoint did not return any results. 
	 * Go to the 'README.md' file in the root folder of the application for further details.
	 * 
	 * 
String queryTotal= "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>
PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  owl:  <http://www.w3.org/2002/07/owl#>
PREFIX  wdt:  <http://www.wikidata.org/prop/direct/>

SELECT DISTINCT  ?id_accident ?street_crossing_label ?district ?postal_code ?population ?image ?localization
WHERE
{ ?accident  rdfs:label   ?id_accident ;
          ont:occursOn  ?street_crossing .
?street_crossing
          rdfs:label    ?street_crossing_label ;
          wdt:P131      ?district_csv .
?district_csv
          rdfs:label    ?district ;
          owl:sameAs    ?district_wikidata
SERVICE <https://query.wikidata.org/sparql>
  { OPTIONAL
      { ?district_wikidata
                  wdt:P1082  ?population
      }
    OPTIONAL
      { ?district_wikidata
                  wdt:P281  ?postal_code
      }
    OPTIONAL
      { ?district_wikidata
                  wdt:P18  ?image
      }
    OPTIONAL
      { ?district_wikidata
                  wdt:P402  ?localization
      }
  }
}
LIMIT   500";

So what we have done is to make a different query to each endpoint (ours and Wikidata's one) 
and program a join through the *District* column as you can see in the code.

	 */


	private static Controller c;

	private String[][] resultadoQueryRDF;
	private String[][] resultadoQueryWikiData;
	private String[][] resultadoTotal;

	private static boolean datosCargados;
	private static boolean datosRecibidos;
	private int numerodeFilas;

	final static String endPointURI = "http://localhost:3030/group09/sparql";
	final static String wikiDataURI = "https://query.wikidata.org/sparql";

	private static ArrayList<RDFNode> tiposAccidente;
	private static ArrayList<RDFNode> tiposRangoEdad;
	private static ArrayList<RDFNode> tiposSexo;
	private static ArrayList<RDFNode> tiposGradoLesion;
	private static ArrayList<RDFNode> tiposMes;
	private static ArrayList<RDFNode> tiposDistrito;
	private static ArrayList<RDFNode> tiposVehiculo;
	private static ArrayList<RDFNode> tiposIntervaloHora;
	private static ArrayList<RDFNode> tiposWeather;


	public Engine() {
		c = Searcher.getC();
		if(!datosCargados) {
			datosRecibidos = false;
			tiposAccidente = new ArrayList<RDFNode>();
			tiposRangoEdad = new ArrayList<RDFNode>();
			tiposSexo = new ArrayList<RDFNode>();
			tiposGradoLesion = new ArrayList<RDFNode>();
			tiposMes = new ArrayList<RDFNode>();
			tiposDistrito = new ArrayList<RDFNode>();
			tiposVehiculo = new ArrayList<RDFNode>();
			tiposIntervaloHora = new ArrayList<RDFNode>();
			tiposWeather = new ArrayList<RDFNode>();
			cargarTipoVehiculo();
			cargarTipoSex();
			cargarTipoEdad();
			cargarTipoLesividad();
			cargarDistritos();
			cargarTiposAccidente();
			cargarMeses();
			cargarWeather();
			cargarHoraIntervalo();
			datosCargados = true;
		}
		if(datosRecibidos) {
			resultadoQueryRDF = new String[Integer.parseInt(c.getS().getN_results())][3];
			resultadoQueryWikiData = new String[tiposDistrito.size()+1][5];
			resultadoTotal = new String[Integer.parseInt(c.getS().getN_results())][7];
			executeRDFQuery();
			executeWikiDataQuery();
			joinResults();
		}	
	}

	private void cargarTipoVehiculo(){
		String queryTipoVehiculo = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n" + 
				"PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?typevehicle_label\r\n" + 
				"WHERE\r\n" + 
				"  { ?vehicle  rdf:type    ont:TypeOfVehicle ;\r\n" + 
				"              rdfs:label  ?typevehicle_label\r\n" + 
				"  }";

		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryTipoVehiculo);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposVehiculo.add(soln.get("?typevehicle_label"));
		}
		q.close();
	}
	private void cargarTipoSex(){
		String querySex = "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"PREFIX  aos:  <http://rdf.muninn-project.org/ontologies/appearances.html#>\r\n" + 
				"PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?sex_label\r\n" + 
				"WHERE\r\n" + 
				"  { ?sex  rdf:type    aos:Sex ;\r\n" + 
				"          rdfs:label  ?sex_label\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, querySex);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposSexo.add(soln.get("?sex_label"));
		}
		q.close();
	}
	private void cargarTipoEdad(){
		String queryRangoEdad = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?age_range\r\n" + 
				"WHERE\r\n" + 
				"  {\r\n" + 
				"    ?person   ont:hasAgeRange  ?age_range\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryRangoEdad);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			tiposRangoEdad.add(soln.get("?age_range"));
		}
		q.close();
	}
	private void cargarTipoLesividad(){
		String queryLesividad = "PREFIX  datex: <http://vocab.datex.org/terms/#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?injury\r\n" + 
				"WHERE\r\n" + 
				"  { ?person  datex:injuryStatus  ?injury }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryLesividad);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposGradoLesion.add(soln.get("?injury"));
		}
		q.close();
	}
	private void cargarDistritos(){
		String queryDistritos = "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"PREFIX  juso: <http://rdfs.co/juso/>\r\n" + 
				"PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?district_label\r\n" + 
				"WHERE\r\n" + 
				"  { ?district  rdf:type           juso:District ;\r\n" + 
				"              rdfs:label          ?district_label .\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryDistritos);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposDistrito.add(soln.get("?district_label"));
		}
		q.close();
	}
	private void cargarTiposAccidente(){
		String queryTiposAccidente = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?typeaccident_label\r\n" + 
				"WHERE\r\n" + 
				"  { ?accident  ont:typeOfAccident  ?typeaccident .\r\n" + 
				"    ?typeaccident\r\n" + 
				"              rdfs:label          ?typeaccident_label\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryTiposAccidente);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposAccidente.add(soln.get("?typeaccident_label"));
		}
		q.close();
	}
	private void cargarMeses(){
		String queryMeses = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?month\r\n" + 
				"WHERE\r\n" + 
				"  { ?accident ont:happensMonth    ?month .\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryMeses);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposMes.add(soln.get("?month"));
		}
		q.close();
	}
	private void cargarWeather(){
		String queryWeather = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?weather\r\n" + 
				"WHERE\r\n" + 
				"  { ?accident ont:weather         ?weather.\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryWeather);  
		ResultSet results = q.execSelect();
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposWeather.add(soln.get("?weather"));
		}
		q.close();
	}
	private void cargarHoraIntervalo(){
		String queryHoraIntervalo = "PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?hour_interval\r\n" + 
				"WHERE\r\n" + 
				"  { ?accident ont:occursAtPeriod  ?hour_interval.\r\n" + 
				"  }";
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI, queryHoraIntervalo);  
		ResultSet results = q.execSelect();

		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			Engine.tiposIntervaloHora.add(soln.get("?hour_interval"));
		}
		q.close();
	}


	private void executeRDFQuery(){

		String paramLimit = " LIMIT " + String.valueOf(c.getS().getN_results());

		String queryRDF= "PREFIX  td:   <https://transportdisruption.github.io/#>\r\n" + 
				"PREFIX  ont:  <http://linkeddata.es/group09/ontology/TrafficAccident#>\r\n" + 
				"PREFIX  aos:  <http://rdf.muninn-project.org/ontologies/appearances.html#>\r\n" + 
				"PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n" + 
				"PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\r\n" + 
				"PREFIX  datex: <http://vocab.datex.org/terms/#>\r\n" + 
				"PREFIX  wdt:  <http://www.wikidata.org/prop/direct/>\r\n" + 
				"PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT ?id_accident ?street_crossing_label ?district\r\n" + 
				"WHERE\r\n" + 
				"  { ?accident  rdf:type             td:Accident ;\r\n" + 
				"              rdfs:label            ?id_accident ;\r\n" + 
				"              ont:occursOn          ?street_crossing ;\r\n" + 
				"              ont:typeOfAccident    ?typeOfAccident ;\r\n" + 
				"              ont:happensMonth      ?month ;\r\n" +  
				"              ont:occursAtPeriod    ?period ;\r\n" + 
				"              ont:occursTo          ?person ;\r\n" +
				"              ont:weather           ?weather .\r\n" + 
				"    ?typeOfAccident\r\n" + 
				"              rdfs:label            ?typeOfAccident_label .\r\n" + 
				"    ?street_crossing\r\n" + 
				"              rdfs:label            ?street_crossing_label ;\r\n" + 
				"              wdt:P131              ?district_csv .\r\n" + 
				"    ?district_csv\r\n" + 
				"              rdfs:label            ?district .\r\n" + 
				"    ?person   ont:hasAgeRange       ?range ;\r\n" + 
				"              datex:injuryStatus    ?injuryStatus ;\r\n" +
				"              aos:hasSex            ?sex ;\r\n" +
				"              ont:hasTypeOfVehicle  ?typeOfVehicle .\r\n" + 
				"    ?sex      rdfs:label            ?sex_label .\r\n" + 
				"    ?typeOfVehicle\r\n" + 
				"              rdfs:label            ?typeOfVehicle_label\r\n" + 
				"  }";

		queryRDF+=paramLimit;


		ParameterizedSparqlString queryRDFParam = new ParameterizedSparqlString(queryRDF);


		if(!c.getS().getDistrito_seleccionado().equals("NO FILTER")){
			queryRDFParam.setLiteral("district", c.getS().getDistrito_seleccionado());
		}
		if(c.getS().getDistrito_seleccionado().equals("San Blas")) {
			c.getS().setDistrito_seleccionado("San Blas-Canillejas");
		}
		if(!c.getS().getGradoLesion_seleccionado().equals("NO FILTER")){
			queryRDFParam.setLiteral("injuryStatus",c.getS().getGradoLesion_seleccionado());
		}
		if(!c.getS().getIntervaloHora_seleccionado().equals("NO FILTER")) {
			queryRDFParam.setLiteral("period",c.getS().getIntervaloHora_seleccionado());
		}
		if(!c.getS().getMes_seleccionado().equals("NO FILTER")) {
			queryRDFParam.setLiteral("month",c.getS().getMes_seleccionado());
		}
		if(!c.getS().getRangoEdad_seleccionado().equals("NO FILTER")) {
			queryRDFParam.setLiteral("range",c.getS().getRangoEdad_seleccionado());
		}
		if(!c.getS().getSexo_seleccionado_seleccionado().equals("NO FILTER")){
			queryRDFParam.setLiteral("sex_label",c.getS().getSexo_seleccionado_seleccionado());
		}
		if(!c.getS().getTipoAccidente_seleccionado().equals("NO FILTER")) {
			queryRDFParam.setLiteral("typeOfAccident_label",c.getS().getTipoAccidente_seleccionado() );
		}
		if(!c.getS().getVehiculo_seleccionado().equals("NO FILTER")){
			queryRDFParam.setLiteral("typeOfVehicle_label",c.getS().getVehiculo_seleccionado());
		}
		if(!c.getS().getWeather_seleccionado().equals("NO FILTER")){
			queryRDFParam.setLiteral("weather",c.getS().getWeather_seleccionado() );
		}



		Query queryRDFparam = QueryFactory.create(queryRDFParam.asQuery()); 
		QueryExecution q = QueryExecutionFactory.sparqlService(endPointURI,queryRDFparam);  
		ResultSet results = q.execSelect();
		int contador=0;
		while (results.hasNext()) {
			QuerySolution soln = results.nextSolution();
			resultadoQueryRDF[contador][0] = soln.get("?id_accident").toString();
			resultadoQueryRDF[contador][1] = soln.get("?street_crossing_label").toString();
			if(c.getS().getDistrito_seleccionado().equals("NO FILTER")){
				resultadoQueryRDF[contador][2] = soln.get("?district").toString();
			}
			else {
				resultadoQueryRDF[contador][2] = c.getS().getDistrito_seleccionado();
			}
			contador++;
		}
		numerodeFilas = contador;
		q.close();
	}
	private void executeWikiDataQuery() {
		String queryWikidata = "PREFIX  wdtn: <http://www.wikidata.org/prop/direct-normalized/>\r\n" + 
				"PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\r\n" + 
				"PREFIX  wd:   <http://www.wikidata.org/entity/>\r\n" + 
				"PREFIX  wdt:  <http://www.wikidata.org/prop/direct/>\r\n" + 
				"\r\n" + 
				"SELECT DISTINCT  ?label ?postal_code ?population ?image ?localization\r\n" + 
				"WHERE\r\n" + 
				"  { ?subject  wdt:P31     wd:Q3032114 ;\r\n" + 
				"              rdfs:label  ?label\r\n" + 
				"    OPTIONAL\r\n" + 
				"      { ?subject  wdt:P1082  ?population }\r\n" + 
				"    OPTIONAL\r\n" + 
				"      { ?subject  wdt:P625  ?coordinates }\r\n" + 
				"    OPTIONAL\r\n" + 
				"      { ?subject  wdt:P281  ?postal_code }\r\n" + 
				"    OPTIONAL\r\n" + 
				"      { ?subject  wdt:P18  ?image }\r\n" + 
				"    OPTIONAL\r\n" + 
				"      { ?subject  wdtn:P402  ?localization }\r\n" +  
				"    FILTER langMatches(lang(?label), \"ES\")\r\n" + 
				"  }";


		QueryExecution q = QueryExecutionFactory.sparqlService(wikiDataURI, queryWikidata);  
		ResultSet results2 = q.execSelect();


		int contador2=0;

		while (results2.hasNext()) {
			QuerySolution soln = results2.nextSolution();
			if(soln.get("?label")!=null) {
				resultadoQueryWikiData[contador2][0] = soln.get("?label").toString();
			}
			else {
				resultadoQueryWikiData[contador2][0]="";
			}
			if (soln.get("?postal_code")!= null){
				resultadoQueryWikiData[contador2][1] = soln.get("?postal_code").toString();
			}
			else {
				resultadoQueryWikiData[contador2][1] = "";
			}
			if(soln.get("?population")!= null) {
				String total = soln.get("?population").toString();
				resultadoQueryWikiData[contador2][2] = total.substring(0, total.indexOf("^"));
			}
			else {
				resultadoQueryWikiData[contador2][2]="";
			}
			if(soln.get("?image") != null) {
				resultadoQueryWikiData[contador2][3] = soln.get("?image").toString();

			}
			else {
				resultadoQueryWikiData[contador2][3]="";
			}
			if(soln.get("?localization") != null) {
				resultadoQueryWikiData[contador2][4] = soln.get("?localization").toString();
			}
			else {
				resultadoQueryWikiData[contador2][4]="";
			}
			contador2++;
		}
		q.close();
	}
	private void joinResults() {
		int contadorTotal=0;
		for(int i=0;i<this.resultadoQueryRDF.length;i++) {
			for(int j=0;j<this.resultadoQueryWikiData.length;j++) {
				if((resultadoQueryRDF[i][2]+"@es").equals(resultadoQueryWikiData[j][0])){
					resultadoTotal[contadorTotal]=  ArrayUtils.addAll(resultadoQueryRDF[i], Arrays.copyOfRange(resultadoQueryWikiData[j], 1, 5));
					contadorTotal++;
				}
			}
		}
	}

	public ArrayList<RDFNode> getTiposAccidente() {
		return tiposAccidente;
	}

	public void setTiposAccidente(ArrayList<RDFNode> tiposAccidente) {
		Engine.tiposAccidente = tiposAccidente;
	}

	public ArrayList<RDFNode> getTiposRangoEdad() {
		return tiposRangoEdad;
	}

	public void setTiposRangoEdad(ArrayList<RDFNode> tiposRangoEdad) {
		Engine.tiposRangoEdad = tiposRangoEdad;
	}

	public ArrayList<RDFNode> getTiposSexo() {
		return tiposSexo;
	}

	public void setTiposSexo(ArrayList<RDFNode> tiposSexo) {
		Engine.tiposSexo = tiposSexo;
	}

	public ArrayList<RDFNode> getTiposGradoLesion() {
		return tiposGradoLesion;
	}

	public void setTiposGradoLesion(ArrayList<RDFNode> tiposGradoLesion) {
		Engine.tiposGradoLesion = tiposGradoLesion;
	}

	public ArrayList<RDFNode> getTiposMes() {
		return tiposMes;
	}

	public void setTiposMes(ArrayList<RDFNode> tiposMes) {
		Engine.tiposMes = tiposMes;
	}

	public ArrayList<RDFNode> getTiposDistrito() {
		return tiposDistrito;
	}

	public void setTiposDistrito(ArrayList<RDFNode> tiposDistrito) {
		Engine.tiposDistrito = tiposDistrito;
	}

	public ArrayList<RDFNode> getTiposVehiculo() {
		return tiposVehiculo;
	}

	public void setTiposVehiculo(ArrayList<RDFNode> tiposVehiculo) {
		Engine.tiposVehiculo = tiposVehiculo;
	}

	public ArrayList<RDFNode> getTiposIntervaloHora() {
		return tiposIntervaloHora;
	}

	public void setTiposIntervaloHora(ArrayList<RDFNode> tiposIntervaloHora) {
		Engine.tiposIntervaloHora = tiposIntervaloHora;
	}

	public ArrayList<RDFNode> getTiposWeather() {
		return tiposWeather;
	}

	public void setTiposWeather(ArrayList<RDFNode> tiposWeather) {
		Engine.tiposWeather = tiposWeather;
	}

	public static Controller getC() {
		return c;
	}

	public static void setC(Controller c) {
		Engine.c = c;
	}

	public String[][] getResultadoQueryRDF() {
		return resultadoQueryRDF;
	}

	public void setResultadoQueryRDF(String[][] resultadoQueryRDF) {
		this.resultadoQueryRDF = resultadoQueryRDF;
	}

	public String[][] getResultadoQueryWikiData() {
		return resultadoQueryWikiData;
	}

	public void setResultadoQueryWikiData(String[][] resultadoQueryWikiData) {
		this.resultadoQueryWikiData = resultadoQueryWikiData;
	}

	public String[][] getResultadoTotal() {
		return resultadoTotal;
	}

	public void setResultadoTotal(String[][] resultadoTotal) {
		this.resultadoTotal = resultadoTotal;
	}


	public void setDatosCargados(boolean datosCargados) {
		Engine.datosCargados = datosCargados;
	}


	public void setDatosRecibidos(boolean datosRecibidos) {
		Engine.datosRecibidos = datosRecibidos;
	}

	public int getNumerodeFilas() {
		return numerodeFilas;
	}

	public void setNumerodeFilas(int numerodeFilas) {
		this.numerodeFilas = numerodeFilas;
	}
}