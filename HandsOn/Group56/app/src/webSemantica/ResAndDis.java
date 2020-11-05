package webSemantica;

import java.util.ArrayList;

public class ResAndDis {
	String resultado;
	boolean Centro;
	boolean Arganzuela;
	
	public ResAndDis (String resultado, boolean Centro, boolean Arganzuela) {
		this.resultado = resultado;
		this.Centro = Centro;
		this.Arganzuela = Arganzuela;
	}
	
	public String getResultado() {
		return resultado;
	}

	public void setResultado(String resultado) {
		this.resultado = resultado;
	}

	public boolean isCentro() {
		return Centro;
	}

	public void setCentro(boolean centro) {
		Centro = centro;
	}

	public boolean isArganzuela() {
		return Arganzuela;
	}

	public void setArganzuela(boolean arganzuela) {
		Arganzuela = arganzuela;
	}

}
