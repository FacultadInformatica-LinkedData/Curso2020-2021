package App;
import java.io.*;
import java.util.Scanner;
import org.apache.jena.query.*;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.RDFNode;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.atlas.logging.LogCtl;
import Queries.FuncionesSparql;


public class App 
{

    public static void main(String[] args) throws IOException{

    	//Se carga el archivo nTriples
        Model model = RDFDataMgr.loadModel("data.nt");


        //Comienza la aplicacion
        System.out.print("\n------------------------------------------------------\n");
        System.out.println("Practica Semantic Web Grupo 10");
        System.out.print("-------------------------------------------------------\n");
        System.out.println("\nPara elegir el tipo de consulta eliga una de las opciones.");

        Scanner scan = new Scanner(System.in);
        String aux = "";
        String error = "Ha ocurrido un error al procesar su consulta";
        
        //Mientras que no se ejecute la opcion de salir se permanece en la aplicacion
        while (!aux.equals("Exit")) 
        {
        	 System.out.print("\n------------------------------------------------------");
        	//Imprime todas las opciones de consultas disponibles
            System.out.println("\n1) Obtener todos los indicadores\n"
            		+ "2) Obtener un numero de indicadores\n"
            		+ "3) Obtener los nombres\n"
            		+ "4) Obtener las medidas de un codigo\n"
            		+ "5) Obtener todos los valores de un año\n"
            		+ "6) Obtener un codigo determinado\n"
            		+ "Exit) Exit");
            System.out.print("------------------------------------------------------\n");
            aux = scan.nextLine();

            //En el caso de que se elija la consulta 1
            if (aux.equals("1")) 
                {
            	//Imprime todos los indicadores
                    Queries.FuncionesSparql.allIndicatorCodes(model);
                } 
            //En el caso de que se elija la consulta 2
                else if (aux.equals("2")) 
                {
                	//Primero se debe introducir el limite deseado
                    System.out.println("Introduzca el numero de codigo que quiere mostrar");
                    //Y a continuacion imprime el numero de codigos que le has dicho
                    Queries.FuncionesSparql.limitIndicatorCodes(model,Integer.parseInt(scan.nextLine()));
                } 
            //En el caso de que se elija la conuslta 3
                else if (aux.equals("3")) 
                {
                	//Imprime los nombres
                	Queries.FuncionesSparql.indicatorCodesNames(model);
                } 
            //En el caso de que se elija la consulta 4
                else if (aux.equals("4")) 
                {
                	//Primero se debe introducir el codigo deseado
                    System.out.println("Introduzca el valor del codigo por teclado");
                    Queries.FuncionesSparql.valuesInYearIndicatorCode(model,scan.nextLine());
                } 
            //Consulta 5
                else if (aux.equals("5")) 
                {
                    //Introducir primero por teclado el año
                    System.out.println("Introduzca el valor del año por teclado");
                    Queries.FuncionesSparql.allValuesInYear(model,scan.nextLine());
                } 
            //Consulta tipo 6
                else if (aux.equals("6")) 
                {
                    //Introducir el codigo por teclado
                    System.out.println("Introduzca el valor del codigo por teclado");
                    Queries.FuncionesSparql.indicatorCodeToName(model,scan.nextLine());
                } 
                else if (aux.equals("Exit")) 
                {
                    // Se sale de la aplicacion
                	System.out.println("Saliendo de la aplicacion");
                   
                } 
                else 
                {
                    System.out.println(error);
                }
           } 
                    
    }

    
}
