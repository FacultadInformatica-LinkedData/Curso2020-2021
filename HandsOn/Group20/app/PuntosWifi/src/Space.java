import java.util.ArrayList;

import org.apache.jena.ontology.OntModel;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.ModelFactory;


public class Space {
	
	private String hasName;
	private ArrayList<String> name;
	private String hasSchedule;
	private String hasEquipment;
	private String hasDescriptionEntity;
	private String hasDescription;
	private String hasRoute;
	private String hasTelephone;
	private String hasAccesibility;
	private String hasURL;
	private String hasEmail;
	private String hasContact;
	private String hasType; //???
	
	private String hasLocation;
	
	private static final String inputFile = "output-with-links.nt";
	
	public Space() {
		
	}
	
	// GETERS DE LOS ATRIBUTOS
	
	public String getHasName() {
		return this.hasName;
	}
	
	public ArrayList<String> getName() {
		return this.name;
	}

	public void setName(ArrayList<String> name) {
		this.name = name;
	}
	
	
	public String getHasSchedule() {
		return this.hasSchedule;
	}
	
	public String getHasEquipment() {
		return this.hasEquipment;
	}
	
	public String getHasDescriptionEntity() {
		return this.hasDescriptionEntity;
	}
	
	public String getHasDescription() {
		return this.hasDescription;
	}
	
	public String getHasRoute() {
		return this.hasRoute;
	}
	
	public String getHasTelephone() {
		return this.hasTelephone;
	}
	
	public String getHasAccesibility() {
		return this.hasAccesibility;
	}
	
	public String getHasURL() {
		return this.hasURL;
	}
	
	public String getHasEmail() {
		return this.hasEmail;
	}
	
	public String getHasContact() {
		return this.hasContact;
	}
	
	public String getHasType() {
		return this.hasType;
	}
	
	public String getHasLocation() {
		return this.hasLocation;
	}
	
	// SETERS DE LOS ATRIBUTOS
	
	public void setHasName(String hasName) {
		this.hasName = hasName;
	}
	
	public void setHasSchedule(String hasSchedule) {
		this.hasSchedule = hasSchedule;
	}
	
	public void setHasEquipment(String hasEquipment) {
		this.hasEquipment = hasEquipment;
	}
	
	public void setHasDescriptionEntity(String hasDescriptionEntity) {
		this.hasDescriptionEntity = hasDescriptionEntity;
	}
	
	public void setHasDescription(String hasDescription) {
		this.hasDescription = hasDescription;
	}
	
	public void setHasRoute(String hasRoute) {
		this.hasRoute = hasRoute;
	}
	
	public void setHasTelephone(String hasTelephone) {
		this.hasTelephone = hasTelephone;
	}
	
	public void setHasAccesibility(String hasAccesibility) {
		this.hasAccesibility = hasAccesibility;
	}
	
	public void setHasURL(String hasURL) {
		this.hasURL = hasURL;
	}
	
	public void setHasEmail(String hasEmail) {
		this.hasEmail = hasEmail;
	}
	
	public void setHasContact(String hasContact) {
		this.hasContact = hasContact;
	}
	
	public void setHasType(String hasType) {
		this.hasType = hasType;
	}
	
	public void setHasLocation(String hasLocation) {
		this.hasLocation = hasLocation;
	}
	
	
	public ArrayList<String> getListSpace(String nombre){
		
		Space space = new Space();
		ArrayList<String> array_nombres = new ArrayList<String>();

	    OntModel model = ModelFactory.createOntologyModel();
	    
	    model.read(inputFile,null,"N-TRIPLES");

	    String queryString=
			"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
					+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
					+ "SELECT DISTINCT ?name WHERE { \n"
					+ "        { ?pred <https://freewifizones/madrid/space#" + nombre + "> ?name. \n"		
					+ "}"
					+ "}";
		Query query= QueryFactory.create(queryString);
		QueryExecution qexec=QueryExecutionFactory.create(query, model);
		
		try {
		    ResultSet results = qexec.execSelect();
		    while ( results.hasNext()){
		        QuerySolution soln = results.nextSolution();
		        array_nombres.add(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			space.setName(array_nombres);
			//System.out.println("\n ++++++++++ \n" + array_nombres.toString());
			qexec.close();
		  }
		
		return array_nombres;
	}
	
	
	public ArrayList<String> getListSpacesNeighboord(String nombre){
		ArrayList<String> array_nombres = new ArrayList<String>();
	    OntModel model = ModelFactory.createOntologyModel();
	    
	    model.read(inputFile,null,"N-TRIPLES");

	    String queryString=
			"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
					+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
					+ "SELECT DISTINCT ?name WHERE { \n"
					+          "{ ?obj <https://freewifizones/madrid/location#neighborhood>" + "\"" + nombre + "\""  +". \n"
					+ "           ?pred <https://freewifizones/madrid/space#hasLocation> ?obj. \n"
					+ "           ?pred <https://freewifizones/madrid/space#hasName> ?name. \n"
					+ "}"
					//+ " ORDER BY ?name. \n"
					+ "}";
		Query query= QueryFactory.create(queryString);
		QueryExecution qexec=QueryExecutionFactory.create(query, model);
		
		try {
		    ResultSet results = qexec.execSelect();
		    while ( results.hasNext()){
		        QuerySolution soln = results.nextSolution();
		        array_nombres.add(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//space.setName(array_nombres);
			//System.out.println("\n ++++++++++ \n" + array_nombres.toString());
			qexec.close();
		  }
		
		return array_nombres;
	}
	
	
	public void getListAttSpace(String nombre){
		
		Query query;
		QueryExecution qexec; 
	    ResultSet results;
        QuerySolution soln;
		

	    OntModel model = ModelFactory.createOntologyModel();
	    model.read(inputFile,null,"N-TRIPLES");

	    String query_hasSchedule=
			"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
					+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
					+ "SELECT DISTINCT ?pred ?name WHERE { \n"
					+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
					+ "           ?obj <https://freewifizones/madrid/space#hasSchedule> ?name. \n"
					+ "}"
					+ "}";
	    
		query =	QueryFactory.create(query_hasSchedule);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		       setHasSchedule(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasSchedule());
			qexec.close();
		  }
	    
	    String query_hasEquipment = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasEquipment> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasEquipment);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasEquipment(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasEquipment());
			qexec.close();
		  }
		    
	    String query_hasDescriptionEntity = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasDescriptionEntity> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasDescriptionEntity);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasDescriptionEntity(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasDescriptionEntity());
			qexec.close();
		  }
	    
	    String query_hasDescription = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasDescription> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasDescription);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasDescription(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasDescription());
			qexec.close();
		  }
	    
	    String query_hasRoute = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasRoute> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasRoute);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasRoute(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasRoute());
			qexec.close();
		  }
	 
	    String query_hasTelephone = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasTelephone> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasTelephone );
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasTelephone(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasTelephone());
			qexec.close();
		  }
	    
	    String query_hasAccesibility = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasAccesibility> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasAccesibility);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasAccesibility(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasAccesibility());
			qexec.close();
		  }

	    String query_hasUrl = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasUrl> ?name. \n"
						+ "}"
						+ "}";

		query =	QueryFactory.create(query_hasUrl);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasURL(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasURL());
			qexec.close();
		  }
		
	    String query_hasEmail = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasEmail> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasEmail);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasEmail(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasEmail());
			qexec.close();
		  }

	    String query_hasContact = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasContact> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasContact);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasContact(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasContact());
			qexec.close();
		  }

	    String query_hasLocation = 
	    		"PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
						+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
						+ "SELECT DISTINCT ?pred ?name WHERE { \n"
						+          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + nombre + "\""  +". \n"
						+ "           ?obj <https://freewifizones/madrid/space#hasLocation> ?name. \n"
						+ "}"
						+ "}";
	    
		query =	QueryFactory.create(query_hasLocation);
		qexec = QueryExecutionFactory.create(query, model);
		
		try {
		    results = qexec.execSelect();
		    while ( results.hasNext()){
		        soln = results.nextSolution();
		       // array_nombres.add(soln.toString().substring(10,soln.toString().length()-2));
		        setHasLocation(soln.toString().substring(11,soln.toString().length()-3));
		        //System.out.println(soln);
		    }
		    
		} finally {
			//System.out.println("\n ++++++++++ \n" + space.getHasLocation());
			qexec.close();
		  }
	
	}
}