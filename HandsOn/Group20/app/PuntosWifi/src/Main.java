import org.apache.jena.ontology.OntModel;
import org.apache.jena.rdf.model.ModelFactory;


public class Main {
	// Variable which charges our rdf file
	//private static final String inputFile = "/Users/usuario/eclipse-workspace/PuntosWifi/src/handsOn.rdf";
	
	public static void main(String[]args) {
		// *We create an Ontology model
		//OntModel model = ModelFactory.createOntologyModel();
		// *Reading our rdf
		//model.read(inputFile,null,"RDF/XML");
		//model.write(System.out,"RDF/XML");
		
		
		
		Interface interfaz = new Interface("Puntos de Wifi Publicos",950,650);
		 
		Space space = new Space();
		
		Location location = new Location();
		
		
		
		interfaz.init(space.getListSpace("hasName"),location.getListDistrict());
        interfaz.setResizable(false);
        interfaz.setVisible(true);    
        
        space.getListSpace("hasName");
        System.out.println(space.getListSpace("hasName"));
        space.getListSpacesNeighboord("Aluche");
        space.getListAttSpace("Biblioteca Pública Municipal - Aluche");
	}	

}