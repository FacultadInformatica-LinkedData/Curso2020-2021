package webSemantica;

import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;
import java.util.ArrayList;
import java.util.List;
public class Queries {

    private static Model model;


//    public static void main(String[] args) {
//        Queries q = new Queries ();
//        String res;
//        ArrayList al = new ArrayList();
//        al = Queries.queryDistritos();
//       res = Queries.queryInfo(20);
//        res = Queries.queryHayPuesto("Latina");
//       res = Queries.queryCount("Centro");
//        System.out.println(al);
//    }

    public Queries () {

        model = ModelFactory.createDefaultModel();
        model.read("webSemantica/output.nt");
    }

    public static ArrayList queryDistritos () {
        String query = "SELECT DISTINCT ?Distrito\r\n" +
                "WHERE {\r\n" +
                "?id <http://www.semantic.web.es/group33/RecargaMadrid/tieneDistrito> ?Distrito\r\n" +
                "}";
        
        QueryExecution qexec = QueryExecutionFactory.create(query, model);
        ArrayList al = new ArrayList();
        try {
            ResultSet results = qexec.execSelect();
            while (results.hasNext()) {
                al.add(results.nextSolution().getLiteral("Distrito"));
            }
        }
            finally {
            qexec.close();
        
            }
        return al;
    }

    public static String queryInfo (int id) {
        String query = "SELECT DISTINCT ?Distrito ?Direccion ?Operador\r\n" +
                " WHERE {\r\n" +
                "<http://www.semantic.web.es/group33/RecargaMadrid/Puesto/" + id + "> <http://www.semantic.web.es/group33/RecargaMadrid/tieneDistrito> ?Distrito.\r\n" +
                "<http://www.semantic.web.es/group33/RecargaMadrid/Puesto/" + id + "> <http://www.semantic.web.es/group33/RecargaMadrid/tieneDireccion> ?Direccion.\r\n" +
                "<http://www.semantic.web.es/group33/RecargaMadrid/Puesto/" + id + "> <http://www.semantic.web.es/group33/RecargaMadrid/tieneOperador> ?Operador.\r\n" +
                "}";
        return ejecucion(query, null);
    }

    public static String queryHayPuesto (String distrito) {
        String query = "SELECT DISTINCT ?Distrito\r\n" +
                "WHERE {\r\n" +
                "<http://www.semantic.web.es/group33/RecargaMadrid/Distrito/" + distrito + "> <http://www.semantic.web.es/group33/RecargaMadrid/nombreDistrito> ?Distrito.\r\n" +
                "}";
        return ejecucion(query, distrito);
    }

    public static String queryCount (String distrito) {
        String query = "SELECT COUNT (?id)\r\n" +
                " WHERE {\r\n" +
                "?id <http://www.semantic.web.es/group33/RecargaMadrid/tieneDistrito> \""+distrito + "\". \r\n"+
                "}";
        return ejecucion(query,null);
    }

    public static String ejecucion (String querystring, String nombreVariable) {
        String res = "";
        Query query = QueryFactory.create(querystring);
        QueryExecution qexec = QueryExecutionFactory.create(query, model);
        try {
            ResultSet results = qexec.execSelect();
            while (results.hasNext()) {
                QuerySolution soln = results.nextSolution();
                Literal name2, name3, name4;
                Literal name1;
                if (soln.contains(".1")){
                    name1 = soln.getLiteral(".1");
                    res += name1;
                    res = res.substring(0,1);
                    res = "Numero Puestos: " + res + "\n";
                }
                if (soln.contains("Distrito")) {
                    name2 = soln.getLiteral("Distrito");
                    res += "Distrito: " + name2 + "\n";
                }

                if (soln.contains("Direccion")) {
                    name3 = soln.getLiteral("Direccion");
                    res += "Direccion: " + name3 + "\n";
                }

                if (soln.contains("Operador")) {
                    name4 = soln.getLiteral("Operador");
                    res += "Operador: " + name4 + "\n";
                }
                res += "------------------------------------------------\n";
            }
            if (nombreVariable != null) {
                if (res == "") {
                    res = "No Existen Puntos Recarga en el distrito "+nombreVariable+".";
                } else {
                    res = "Existe un Punto Recarga en el distrito \""+nombreVariable+"\".";
                }
            }
        } finally {
            qexec.close();
        }
        return res;
    }
}