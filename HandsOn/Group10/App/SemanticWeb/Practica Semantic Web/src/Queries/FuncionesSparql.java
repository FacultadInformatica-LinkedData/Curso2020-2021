package Queries;
import org.apache.jena.query.Query;
import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.QueryFactory;
import org.apache.jena.query.QuerySolution;
import org.apache.jena.query.ResultSet;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.RDFNode;

public class FuncionesSparql 
{

	//Metodo para realizar la consulta sparql y obtener todos los indicadores
    public static void allIndicatorCodes(Model model) 
    {
    	//Consulta sparql
        String sparql = "PREFIX  base: <ns:>\n"
                + "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                + "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
                + "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
                + "SELECT DISTINCT  ?codigo \n"
                + "WHERE\n"
                + "  { ?o base:hasIndicator ?indicator .\n"
                + "    ?indicator base:indicatorCode ?codigo \n"
                + "  }";

        Query query = QueryFactory.create(sparql);
        QueryExecution exec = QueryExecutionFactory.create(query, model);
        ResultSet res = exec.execSelect();
        System.out.println("El resultado de su consulta es el siguiente\n");
        while(res.hasNext()) {

            QuerySolution sol = res.nextSolution();
            RDFNode codigo = sol.get("?codigo");
            System.out.println("Codigo del indicador: " + codigo.toString());

        }
    }

    //Metodo para realizar la consulta sparql y obtener  un numero de indicadores
    public static void limitIndicatorCodes(Model model, Integer numLimit) 
    {
    	//Consulta sparql
        String sparql = "PREFIX  base: <ns:>\n"
                + "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                + "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
                + "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
                + "SELECT DISTINCT  ?codigo \n"
                + "WHERE\n"
                + "  { ?o base:hasIndicator ?indicator .\n"
                + "    ?indicator base:indicatorCode ?codigo \n"
                + "  }"
                + "LIMIT" + numLimit;

        Query query = QueryFactory.create(sparql);
        QueryExecution exec = QueryExecutionFactory.create(query, model);
        ResultSet res = exec.execSelect();
        System.out.println("El resultado de su consulta es el siguiente\n");
        while(res.hasNext()) {

            QuerySolution sol = res.nextSolution();
            RDFNode codigo = sol.get("?codigo");
            System.out.println("Codigo del indicador: " + codigo.toString());

        }
    }

    //Metodo para realizar la consulta sparql y obtener todos los indicatorNames(nombres)
    public static void indicatorCodesNames(Model model) 
    {
    	//Consulta sparql
       	    String sparql = "PREFIX  base: <ns:>\n"
				+ "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                    + "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
				+ "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
				+ "SELECT DISTINCT  ?codigo ?nombre \n"
				+ "WHERE\n"
				+ "  { ?o base:hasIndicator ?indicator .\n"
				+ "    ?indicator base:indicatorName ?nombre .\n"
				+ "    ?indicator base:indicatorCode ?codigo \n"
				+ "  }";

        Query query = QueryFactory.create(sparql);
        QueryExecution exec = QueryExecutionFactory.create(query, model);
        ResultSet res = exec.execSelect();
        System.out.println("El resultado de su consulta es el siguiente\n");
        while(res.hasNext()) {
            QuerySolution sol = res.nextSolution();
            RDFNode codigo = sol.get("?codigo");
            RDFNode nombre = sol.get("?nombre");
            System.out.println("El indicador con codigo: " + codigo.toString() + ",     representa: " + nombre.toString());
        }
    }

    //Metodo para realizar la consulta sparql y obtener todos las medidas
    public static void valuesInYearIndicatorCode(Model model, String code) 
    {
    	//Consulta sparql
        String sparql = "PREFIX  base: <ns:>\n"
                + "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                + "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
                + "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
                + "SELECT DISTINCT  ?date ?valor \n"
                + "WHERE\n"
                + "  { ?o base:hasIndicator ?indicator .\n"
                + "    ?indicator base:indicatorCode ?codigo .\n"
                + "    ?indicator base:hasMeasure ?medida .\n"
                + "    ?medida base:value ?valor .\n"
                + "    ?medida base:date ?date .\n"
                + " FILTER regex(str(?codigo), \"" + code + "\")"
                + "  }";

        Query query = QueryFactory.create(sparql);
        QueryExecution exec = QueryExecutionFactory.create(query, model);
        ResultSet res = exec.execSelect();

        System.out.println("Las mediciones para el codigo " + code + " son :");
        System.out.println("El resultado de su consulta es el siguiente\n");
        while (res.hasNext()) {
            QuerySolution sol = res.nextSolution();
            RDFNode codigo = sol.get("?date");
            RDFNode valor = sol.get("?valor");

            System.out.println("Año: " + codigo.toString() + ",     valor: " + valor.toString());

        }
    }

    //Metodo para realizar la consulta sparql y obtener todos los valores de un año
    public static void allValuesInYear(Model model, String filtro) {

        if(Integer.parseInt(filtro)<1960 || Integer.parseInt(filtro)>2018) {
            System.out.println("fecha fuera de rango");
        }
        else {
        	//Consulta sparql
            String sparql = "PREFIX  base: <ns:>\n"
                    + "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
                    + "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
                    + "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
                    + "SELECT DISTINCT  ?date ?codigo ?valor \n"
                    + "WHERE\n"
                    + "  { ?o base:hasIndicator ?indicator .\n"
                    + "    ?indicator base:indicatorCode ?codigo .\n"
                    + "    ?indicator base:hasMeasure ?medida .\n"
                    + "    ?medida base:date ?date .\n"
                    + "    ?medida base:value ?valor .\n"
                    + " FILTER regex(str(?date), \""+ filtro +"\")"
                    + "  }";


            Query query = QueryFactory.create(sparql);
            QueryExecution exec = QueryExecutionFactory.create(query, model);
            ResultSet res = exec.execSelect();
            System.out.println("El resultado de su consulta es el siguiente\n");
            while(res.hasNext()) {
                QuerySolution sol = res.nextSolution();
                RDFNode codigo = sol.get("?codigo");
                RDFNode valor = sol.get("?valor");


                System.out.println("Año: " + filtro + "\t Codigo de indicador: "+ codigo.toString() + ",\t y el valor de la mediciÃ³n es: " + valor.toString());
            }
        }
    }
    
    //Metodo para realizar la consulta sparql y obtener el nombre de codigo
    public static void indicatorCodeToName(Model model, String filtro) 
    {

	if(filtro.equals("")) {
		System.out.println("No ha introducido ningun codigo");
	}
	else {
		String sparql = "PREFIX  base: <ns:>\n"
				+ "PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n"
				+ "PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
				+ "PREFIX  owl:  <http://www.w3.org/2002/07/owl#>\n"
				+ "SELECT DISTINCT  ?codigo ?nombre \n"
				+ "WHERE\n"
				+ "  { ?o base:hasIndicator ?indicator .\n"
				+ "    ?indicator base:indicatorName?nombre .\n"
				+ "    ?indicator base:indicatorCode ?codigo \n"
				+ " FILTER regex(str(?codigo), \""+ filtro +"\")"	
				+ "  }";

    	Query consulta = QueryFactory.create(sparql);
        QueryExecution ejecucion = QueryExecutionFactory.create(consulta, model);
        ResultSet resultados = ejecucion.execSelect();
        System.out.println("El resultado de su consulta es el siguiente\n");

    	while(resultados.hasNext()) {
			QuerySolution solucion = resultados.nextSolution();
			RDFNode codigo = solucion.get("?codigo");
			RDFNode nombre = solucion.get("?nombre");
			
			
			System.out.println("El indicador: " + codigo.toString() + ", representa: " + nombre.toString());
			
	
		}
	}
    }
	
}
