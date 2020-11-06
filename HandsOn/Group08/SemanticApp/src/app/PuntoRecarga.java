package app;

public class PuntoRecarga {
	private String calle;
	private String conector;
	private String distrito;
	private String potencia;
	private String coordX;
	private String coordY;
	private String edificio;
	private String terminal;
	
	public PuntoRecarga() {
		
	}
	
	public PuntoRecarga(String calle, String conector, String distrito, String potencia, String coordX, String coordY, String edificio, String terminal){
	    this.calle = calle;
	    this.conector = conector;
	    this.distrito = distrito;
	    this.potencia = potencia;
	    this.coordX = coordX;
	    this.coordY = coordY;
	    this.edificio = edificio;
	    this.terminal = terminal;

	}
	
	public String getEdificio() {
		return edificio;
	}
	public void setEdificio(String edificio) {
		this.edificio = edificio;
	}
	public String getTerminal() {
		return terminal;
	}
	public void setTerminal(String terminal) {
		this.terminal = terminal;
	}
	public String getCalle() {
		return calle;
	}
	public void setCalle(String calle) {
		this.calle = calle;
	}
	public String getConector() {
		return conector;
	}
	public void setConector(String conector) {
		this.conector = conector;
	}
	public String getDistrito() {
		return distrito;
	}
	public void setDistrito(String distrito) {
		this.distrito = distrito;
	}
	public String getPotencia() {
		return potencia;
	}
	public void setPotencia(String potencia) {
		this.potencia = potencia;
	}
	public String getCoordX() {
		return coordX;
	}
	public void setCoordX(String coordX) {
		this.coordX = coordX;
	}
	public String getCoordY() {
		return coordY;
	}
	public void setCoordY(String coordY) {
		this.coordY = coordY;
	}
}
