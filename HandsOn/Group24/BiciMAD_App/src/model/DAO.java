package model;

import java.io.InputStream;
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

public class DAO {
    
    // Attributes
    static Model model;
    
    // Contstructor
    @SuppressWarnings("deprecation")
    public DAO(){
        // Read the data and save the graph
	Model model = ModelFactory.createDefaultModel();
	InputStream in = FileManager.get().open("src/resources/data.nt");
	model.read(in, null, "N-TRIPLES");
        this.model = model;
    }
    			
    // Main methods
    public static HashMap<String, String> getDistricts(){
        String queryString = "SELECT ?URI ?x {" + 
                                "?URI <http://www.semanticweb.org/bicimad/properties#district_name> ?x}";
        HashMap<String, String> districts = consultWithSparql(queryString);
	return districts;
    }	
    
    public static HashMap<String, String> getNeighbourhoods(String districtURI){
        String queryString = "SELECT ?URI ?x {" + 
                                "?URI <http://www.semanticweb.org/bicimad/properties#has_district> " + districtURI + "." + 
                                "?URI <http://www.semanticweb.org/bicimad/properties#neighbourhood_name> ?x}";
	HashMap<String, String> neighbourhoods = consultWithSparql(queryString);
	return neighbourhoods;
    }	
			
    public static HashMap<String, String> getAddresses(String neighbourhoodURI){
        String queryString = "SELECT ?URI ?x {" + 
                                "?streetURI <http://www.semanticweb.org/bicimad/properties#has_neighbourhood> " + neighbourhoodURI + "." + 
                                "?URI <http://www.semanticweb.org/bicimad/properties#has_street> ?streetURI ." + 
                                "?URI <http://www.semanticweb.org/bicimad/properties#has_address> ?x}";
        HashMap<String, String> addresses = consultWithSparql(queryString);
        return addresses;
    }
    
    
    // Auxiliar methods
    public static String[] getNames(HashMap<String, String> map){
        String[] names = new String[map.size()];
        Iterator<String> results = map.keySet().iterator();
        String aux;
        int i = 0;
        while(results.hasNext()) {
            names[i] = results.next();
            i++;
        }
        return names;
    }
    
    
    private static HashMap<String, String> consultWithSparql(String queryString){
	Query query = QueryFactory.create(queryString);
	QueryExecution qexec = QueryExecutionFactory.create(query, model);
	HashMap<String, String> mapResult = new HashMap<>();
		
	QuerySolution result;
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

    // To check the results before develop the view
    private static void printResults(HashMap<String, String> toPrint) {
        Iterator<String> results = toPrint.keySet().iterator();
        String aux;
        while(results.hasNext()) {
            aux = results.next();
            System.out.println(aux + ": " + toPrint.get(aux));
        }
    } 
}
