package webSemantica;

import java.util.ArrayList;

import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;

public class Queries {

	private static Model model;

	public Queries () {
		model = ModelFactory.createDefaultModel();
		model.read("output.nt");
	}

	//	// Despliegue de distrito
	//	public static String queryDespliegueD () {
	//		return "SELECT DISTINCT ?Distrito\r\n" + 
	//				"WHERE {\r\n" + 
	//				"	?Distrito a <http://group56.org/zonas-verdes/Distrito>.\r\n" + 
	//				"}";
	//	}

	public static ResAndDis queryNarchivo (int narchivo) {
		String query = "SELECT DISTINCT ?D ?S ?Calle ?Destino ?Naturaleza ?Solar ?Apartado\r\n" + 
				"WHERE {\r\n" + 
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/tieneDistrito> ?Distrito.\r\n" + 
				"?Distrito <http://group56.org/zonas-verdes/nombreDistrito> ?D." +
				"?Distrito <http://group56.org/zonas-verdes/tieneSubepigrafe> ?Subepigrafe." +
				"?Subepigrafe  <http://group56.org/zonas-verdes/nombreSubepigrafe> ?S." +
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/nombreCalle> ?Calle." +
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/nombreDestino> ?Destino." +
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/nombreNaturaleza> ?Naturaleza." +
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/tamanioSolar> ?Solar." +
				"<http://group56.org/zonas-verdes/Numero_de_archivo/" + narchivo + "> <http://group56.org/zonas-verdes/nombreApartado>  ?Apartado." +
				"}";
		return ejecucion(query, null, narchivo);
	}

	public static ResAndDis queryDistrito (String distrito) {
		String query = "SELECT DISTINCT ?Calle ?N ?Destino ?Naturaleza ?Solar ?Apartado ?S\r\n" + 
				" WHERE {\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/tieneDistrito> <http://group56.org/zonas-verdes/Distrito/"+ distrito +">.\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/nombreCalle> ?Calle." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreDestino> ?Destino." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreNaturaleza> ?Naturaleza." +
				"?Narchivo <http://group56.org/zonas-verdes/tamanioSolar> ?Solar." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreApartado>  ?Apartado." +
				"<http://group56.org/zonas-verdes/Distrito/"+ distrito +"> <http://group56.org/zonas-verdes/tieneSubepigrafe> ?Subepigrafe." +
				"?Subepigrafe  <http://group56.org/zonas-verdes/nombreSubepigrafe> ?S." +
				"?Narchivo <http://group56.org/zonas-verdes/numeroArchivo> ?N." +
				"}";
		return ejecucion(query, distrito, -1);
	}

	public static ResAndDis querySolar (int solarmenor, int solarmayor) {
		String query = "SELECT DISTINCT ?D ?Calle ?N ?Destino ?Naturaleza ?Solar ?Apartado ?S\r\n" + 
				" WHERE {\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/tamanioSolar> ?Solar." +
				"?Narchivo <http://group56.org/zonas-verdes/tieneDistrito> ?Distrito.\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/nombreCalle> ?Calle." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreDestino> ?Destino." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreNaturaleza> ?Naturaleza." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreApartado>  ?Apartado." +
				"?Distrito <http://group56.org/zonas-verdes/nombreDistrito> ?D." +
				"?Distrito <http://group56.org/zonas-verdes/tieneSubepigrafe> ?Subepigrafe." +
				"?Subepigrafe  <http://group56.org/zonas-verdes/nombreSubepigrafe> ?S." +
				"?Narchivo <http://group56.org/zonas-verdes/numeroArchivo> ?N.";
		if (solarmenor >= 0) {
			query += "FILTER ("+ solarmenor + "<= ?Solar).";
		}
		if (solarmayor >= 0) {
			query += "FILTER ("+ solarmayor + ">= ?Solar).";
		}
		query += "}";
		return ejecucion(query, null, -1);
	}

	public static ResAndDis queryDS (String distrito, int solarmenor, int solarmayor) {
		String query ="SELECT DISTINCT ?D ?Calle ?N ?Destino ?Naturaleza ?Solar ?Apartado ?S\r\n" + 
				" WHERE {\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/tieneDistrito> <http://group56.org/zonas-verdes/Distrito/"+ distrito +">.\r\n" + 
				"?Narchivo <http://group56.org/zonas-verdes/nombreCalle> ?Calle." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreDestino> ?Destino." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreNaturaleza> ?Naturaleza." +
				"?Narchivo <http://group56.org/zonas-verdes/tamanioSolar> ?Solar." +
				"?Narchivo <http://group56.org/zonas-verdes/nombreApartado>  ?Apartado." +
				"<http://group56.org/zonas-verdes/Distrito/"+ distrito +"> <http://group56.org/zonas-verdes/tieneSubepigrafe> ?Subepigrafe." +
				"?Subepigrafe  <http://group56.org/zonas-verdes/nombreSubepigrafe> ?S." +
				"?Narchivo <http://group56.org/zonas-verdes/numeroArchivo> ?N." +
				"<http://group56.org/zonas-verdes/Distrito/"+ distrito +"> <http://group56.org/zonas-verdes/nombreDistrito> ?D.";
		if (solarmenor >= 0) {
			query += "FILTER ("+ solarmenor + "<= ?Solar).";
		}
		if (solarmayor >= 0) {
			query += "FILTER ("+ solarmayor + ">= ?Solar).";
		}
		query += "}";
		return ejecucion(query, distrito, -1);
	}

	public static ResAndDis ejecucion (String querystring, String distrito, int narchivo) {
		String res = "";
		ResAndDis rad= new ResAndDis(res, false, false);
		Query query = QueryFactory.create(querystring);
		QueryExecution qexec = QueryExecutionFactory.create(query, model);
		try {
			ResultSet results = qexec.execSelect();
			while (results.hasNext()) {
				QuerySolution soln = results.nextSolution();
				Literal name2;
				if(narchivo == -1) {
					name2 = soln.getLiteral("N");
					res += "Número de archivo: " + name2 + "\n";
				}
				else {
					res += "Número de archivo: " + narchivo + "\n";
				}
				if(distrito == null) {
					name2 = soln.getLiteral("D");
					res += "Distrito: " + name2 + "\n";
					if(name2.getString().equals("Centro"))
						rad.Centro = true;
					if(name2.getString().equals("Arganzuela"))
						rad.Arganzuela = true;
				}
				else {
					if(distrito.equals("Centro"))
						rad.Centro = true;
					if(distrito.equals("Arganzuela"))
						rad.Arganzuela = true;
					res += "Distrito: " + distrito + "\n";
				}
				name2 = soln.getLiteral("S");
				res += "Subepígrafe: " + name2 + "\n";
				name2 = soln.getLiteral("Apartado");
				res += "Apartado: " + name2 + "\n";
				name2 = soln.getLiteral("Naturaleza");
				res += "Naturaleza: " + name2 + "\n";
				name2 = soln.getLiteral("Calle");
				res += "Calle: " + name2 + "\n";
				name2 = soln.getLiteral("Destino");
				res += "Destino: " + name2 + "\n";
				name2 = soln.getLiteral("Solar");
				res += "Tamaño solar: " + name2.getDouble() + " m2" + "\n";

				res += "------------------------------------------------\n";
			}
		} finally {
			qexec.close();
		}	
		rad.setResultado(res);
		return rad;
	}

//	public static void main(String[] args) {
//		int narchivo = 300002;
//		String distrito = "Centro";
//		int solarmenor = 100000;
//		int solarmayor = 500000;
//		Queries q = new Queries ();
//		ResAndDis res;
//				res = Queries.queryDistrito(distrito);
//		//		res = Queries.queryNarchivo(narchivo);
//		//		res = Queries.querySolar(solarmenor, solarmayor);
//		//		res = Queries.queryDS(distrito, solarmenor, solarmayor);
//		System.out.println(res.getResultado());
//		System.out.println(res.Centro);
//		System.out.println(res.Arganzuela);
//	}
	
}
