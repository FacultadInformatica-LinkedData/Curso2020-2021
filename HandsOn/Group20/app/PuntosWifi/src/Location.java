import java.util.ArrayList;

import org.apache.jena.ontology.OntModel;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.ModelFactory;


public class Location {
	
	// Variables for Location Class
	private String coordinates, geographicalCoordinates;
	private String address, addressName, addressType, typeNum, floor, orientation, latitude, longitude,
						locality, province;
	private String neighborhood;
	private String district;
	private String num, cp, xcoordinate, ycoordinate;
	
	// Input file for testing
	private static final String inputFile = "output-with-links.nt";
	
	// Method which returns an ArrayList with districts of madrid
	public ArrayList<String> getListDistrict() {
		
		ArrayList<String> districtList = new ArrayList<String>();
				
		OntModel model = ModelFactory.createOntologyModel();
		
		model.read(inputFile,null,"N-TRIPLES");
		
		
		String queryInstruction = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { ?pred <https://freewifizones/madrid/location#district> ?name \n"
				+ "}"
				+ "}";
		
		Query query = QueryFactory.create(queryInstruction);
		QueryExecution qexec = QueryExecutionFactory.create(query,model);
		
		try {
			ResultSet results = qexec.execSelect();
			while(results.hasNext()) {
				QuerySolution sol = results.nextSolution();
				districtList.add(sol.toString().substring(11,sol.toString().length()-3));
			}
			System.out.println(districtList);
		} finally {
			qexec.close();
		}
		return districtList;
	}
	
	// Method which returns an Arraylist of neighbohood. String name = Name of district
	public ArrayList<String> getListNeighborhood (String name) {
			
			ArrayList<String> neighborhoodList = new ArrayList<String>();
						
			OntModel model = ModelFactory.createOntologyModel();
			
			model.read(inputFile,null,"N-TRIPLES");
									
			String queryInstruction = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
					+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
					+ "SELECT DISTINCT ?name \n"
					+ "    WHERE {\n"
					+ "        { ?obj <https://freewifizones/madrid/location#district>"+"\"" + name + "\""+".\n"
					+ "        { ?obj <https://freewifizones/madrid/location#neighborhood> ?name .\n"
					+ "}"
					+ "}"
					+ "}";
			
			Query query = QueryFactory.create(queryInstruction);
			QueryExecution qexec = QueryExecutionFactory.create(query,model);
			
			try {
				ResultSet results = qexec.execSelect();
				while(results.hasNext()) {
					QuerySolution sol = results.nextSolution();
					neighborhoodList.add(sol.toString().substring(11,sol.toString().length()-3));
				}
				System.out.println(neighborhoodList);
			} finally {
				qexec.close();
			}
			return neighborhoodList;
		}
	
	// Method which return uri location for obtain attributes of a library. String name = Biblioteca ...
	public String getCoordinates(String name) {
        Query query;
        QueryExecution qexec; 
        ResultSet results;
        QuerySolution soln;
        OntModel model = ModelFactory.createOntologyModel();
        model.read(inputFile,null,"N-TRIPLES");
        String res = null;
        String query_hasLocation = 
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \n"
                        + "PREFIX owl: <http://www.w3.org/2002/07/owl#> \n"
                        + "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \n"
                        + "SELECT DISTINCT ?pred ?name WHERE { \n"
                        +          "{ ?obj <https://freewifizones/madrid/space#hasName>" + "\"" + name + "\"" + ". \n"
                        + "           ?obj <https://freewifizones/madrid/space#hasLocation> ?name. \n"
                        + "}"
                        + "}";

        query =    QueryFactory.create(query_hasLocation);
        qexec = QueryExecutionFactory.create(query, model);

        try {
            results = qexec.execSelect();
            while ( results.hasNext()){
                soln = results.nextSolution();
                res = "<"+ soln.toString().substring(11,soln.toString().length()-3) +">";
            }
            System.out.println(res);
        } finally {
            qexec.close();
          }

        return res;
    }

	// Method which returns in getters the attributes for a building. String name = getCoordinates(Biblioteca...)
	public void getListAttLocation(String name){
								
		OntModel model = ModelFactory.createOntologyModel();
		
		model.read(inputFile,null,"N-TRIPLES");
		
		// Query for full Address
		String queryAddress = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#address>" +"?name" + ".\n"
				+ "}"
				+ "}";
		
		// Query for Address name
		String queryAddressName = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#addressName>" + "?name" + ".\n"
				+ "}"
				+ "}";
		
		// Quey for Address Type
		String queryAddressType = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#addressType>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for typeNum
		String queryAddressTypeNum = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#typeNum>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for Num
		String queryAddressNum = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#num>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for locality
		String queryAddressLocality = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#locality>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for province
		String queryAddressProvince = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#province>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for postal code
		String queryAddressPostalCode = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#cp>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for neighborhood
		String queryAddressNeighborhood = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#neighborhood>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for district
		String queryAddressDistrict = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#district>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for xcoordinate
		String queryAddressXcoordinate = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#xcoordinate>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for ycoordinate
		String queryAddressYcoordinate = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#ycoordinate>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for latitude
		String queryAddressLatitude = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#latitude>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for longitude
		String queryAddressLongitude = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#longitude>" + "?name" + ".\n"
				+ "}"
				+ "}";
		// Query for geographicalCoordinates
		String queryAddressGeographicalCoordinates = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n"
				+ "PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
				+ "SELECT DISTINCT ?name \n"
				+ "    WHERE {\n"
				+ "        { "+ name + "<https://freewifizones/madrid/location#geographicalCoordinates>" + "?name" + ".\n"
				+ "}"
				+ "}";
		
		// Creating all querys for its execution
		Query query1 = QueryFactory.create(queryAddress);
		Query query2 = QueryFactory.create(queryAddressName);
		Query query3 = QueryFactory.create(queryAddressType);
		Query query4 = QueryFactory.create(queryAddressTypeNum);
		Query query5 = QueryFactory.create(queryAddressNum);
		Query query6 = QueryFactory.create(queryAddressLocality);
		Query query7 = QueryFactory.create(queryAddressProvince);
		Query query8 = QueryFactory.create(queryAddressPostalCode);
		Query query9 = QueryFactory.create(queryAddressNeighborhood);
		Query query10 = QueryFactory.create(queryAddressDistrict);
		Query query11 = QueryFactory.create(queryAddressXcoordinate);
		Query query12 = QueryFactory.create(queryAddressYcoordinate);
		Query query13 = QueryFactory.create(queryAddressLatitude);
		Query query14 = QueryFactory.create(queryAddressLongitude);
		Query query15 = QueryFactory.create(queryAddressGeographicalCoordinates);

		// Associating querys with models
		QueryExecution qexec1 = QueryExecutionFactory.create(query1,model);
		QueryExecution qexec2 = QueryExecutionFactory.create(query2,model);
		QueryExecution qexec3 = QueryExecutionFactory.create(query3,model);
		QueryExecution qexec4 = QueryExecutionFactory.create(query4,model);
		QueryExecution qexec5 = QueryExecutionFactory.create(query5,model);
		QueryExecution qexec6 = QueryExecutionFactory.create(query6,model);
		QueryExecution qexec7 = QueryExecutionFactory.create(query7,model);
		QueryExecution qexec8 = QueryExecutionFactory.create(query8,model);
		QueryExecution qexec9 = QueryExecutionFactory.create(query9,model);
		QueryExecution qexec10 = QueryExecutionFactory.create(query10,model);
		QueryExecution qexec11= QueryExecutionFactory.create(query11,model);
		QueryExecution qexec12= QueryExecutionFactory.create(query12,model);
		QueryExecution qexec13= QueryExecutionFactory.create(query13,model);
		QueryExecution qexec14= QueryExecutionFactory.create(query14,model);
		QueryExecution qexec15= QueryExecutionFactory.create(query15,model);

		// Testing
		try {
			ResultSet results1 = qexec1.execSelect();
			ResultSet results2 = qexec2.execSelect();
			ResultSet results3 = qexec3.execSelect();
			ResultSet results4 = qexec4.execSelect();
			ResultSet results5 = qexec5.execSelect();
			ResultSet results6 = qexec6.execSelect();
			ResultSet results7 = qexec7.execSelect();
			ResultSet results8 = qexec8.execSelect();
			ResultSet results9 = qexec9.execSelect();
			ResultSet results10 = qexec10.execSelect();
			ResultSet results11 = qexec11.execSelect();
			ResultSet results12 = qexec12.execSelect();
			ResultSet results13 = qexec13.execSelect();
			ResultSet results14 = qexec14.execSelect();
			ResultSet results15 = qexec15.execSelect();


			while(results1.hasNext() && results2.hasNext() && results3.hasNext() && results4.hasNext() && results5.hasNext()
					&& results6.hasNext() && results7.hasNext() && results8.hasNext() && results9.hasNext() && results10.hasNext()
					&& results11.hasNext() && results12.hasNext() && results13.hasNext() && results14.hasNext() && results15.hasNext()) {
				
				QuerySolution sol1 = results1.nextSolution();
				QuerySolution sol2 = results2.nextSolution();
				QuerySolution sol3 = results3.nextSolution();
				QuerySolution sol4 = results4.nextSolution();
				QuerySolution sol5 = results5.nextSolution();
				QuerySolution sol6 = results6.nextSolution();
				QuerySolution sol7 = results7.nextSolution();
				QuerySolution sol8 = results8.nextSolution();
				QuerySolution sol9 = results9.nextSolution();
				QuerySolution sol10 = results10.nextSolution();
				QuerySolution sol11 = results11.nextSolution();
				QuerySolution sol12 = results12.nextSolution();
				QuerySolution sol13= results13.nextSolution();
				QuerySolution sol14= results14.nextSolution();
				QuerySolution sol15 = results15.nextSolution();

				// Set the attributes in its setter
				setAddress(sol1.toString().substring(11,sol1.toString().length()-3));
                setAddressName(sol2.toString().substring(11,sol2.toString().length()-3));
                setAddressType(sol3.toString().substring(11,sol3.toString().length()-3));
                setTypeNum(sol4.toString().substring(11,sol4.toString().length()-3));
                setNum(sol5.toString().substring(10,sol5.toString().length()-2)); //sssssssssssssssss
                set_locality_(sol6.toString().substring(11,sol6.toString().length()-3));
                set_province_(sol7.toString().substring(11,sol7.toString().length()-3));
                setCp(sol8.toString().substring(11,sol8.toString().length()-3));
                set_neighborhood_(sol9.toString().substring(11,sol9.toString().length()-3));
                set_district_(sol10.toString().substring(11,sol10.toString().length()-3));
                setXcoordinate(sol11.toString().substring(11,sol11.toString().length()-3));
                setYcoordinate(sol12.toString().substring(11,sol12.toString().length()-3));
                setLatitude(sol13.toString().substring(11,sol13.toString().length()-3));
                setLongitude(sol14.toString().substring(11,sol14.toString().length()-3));
                setGeographicalCoordinates(sol15.toString().substring(11,sol15.toString().length()-3));
				

			}
			
		} finally {
			// Closing all querys
			qexec1.close();
			qexec2.close();
			qexec3.close();
			qexec4.close();
			qexec5.close();
			qexec6.close();
			qexec7.close();
			qexec8.close();
			qexec9.close();
			qexec10.close();
			qexec11.close();
			qexec12.close();
			qexec13.close();
			qexec14.close();
			qexec15.close();

		}		
	}
	
	// Getters and Setters
	public String getCoordinates() {
		return coordinates;
	}
	public void setCoordinates(String coordinates) {
		this.coordinates = coordinates;
	}
	public String getGeographicalCoordinates() {
		return geographicalCoordinates;
	}
	public void setGeographicalCoordinates(String geographicalCoordinates) {
		this.geographicalCoordinates = geographicalCoordinates;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getAddressName() {
		return addressName;
	}
	public void setAddressName(String addressName) {
		this.addressName = addressName;
	}
	public String getAddressType() {
		return addressType;
	}
	public void setAddressType(String addressType) {
		this.addressType = addressType;
	}
	public String getTypeNum() {
		return typeNum;
	}
	public void setTypeNum(String typeNum) {
		this.typeNum = typeNum;
	}
	public String getFloor() {
		return floor;
	}
	public void setFloor(String floor) {
		this.floor = floor;
	}
	public String getOrientation() {
		return orientation;
	}
	public void setOrientation(String orientation) {
		this.orientation = orientation;
	}
	public String getLatitude() {
		return latitude;
	}
	public void setLatitude(String latitude) {
		this.latitude = latitude;
	}
	public String getLongitude() {
		return longitude;
	}
	public void setLongitude(String longitude) {
		this.longitude = longitude;
	}
	public String get_locality_() {
		return locality;
	}
	public void set_locality_(String _locality_) {
		this.locality = _locality_;
	}
	public String get_province_() {
		return province;
	}
	public void set_province_(String _province_) {
		this.province = _province_;
	}
	public String get_neighborhood_() {
		return neighborhood;
	}
	public void set_neighborhood_(String _neighborhood_) {
		this.neighborhood = _neighborhood_;
	}
	public String get_district_() {
		return district;
	}
	public void set_district_(String _district_) {
		this.district = _district_;
	}
	public String getNum() {
		return num;
	}
	public void setNum(String num) {
		this.num = num;
	}
	public String getCp() {
		return cp;
	}
	public void setCp(String cp) {
		this.cp = cp;
	}
	public String getXcoordinate() {
		return xcoordinate;
	}
	public void setXcoordinate(String xcoordinate) {
		this.xcoordinate = xcoordinate;
	}
	public String getYcoordinate() {
		return ycoordinate;
	}
	public void setYcoordinate(String ycoordinate) {
		this.ycoordinate = ycoordinate;
	}
		
}
