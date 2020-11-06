package controlador;

import gui.Result;
import gui.Searcher;
import modelo.Engine;

public class Controller {

	private static Engine e;
	private static Searcher s;	
	private static Result r;


	public Controller() {
		e = new Engine();
	}

	public Engine getE() {
		return e;
	}

	public void setE(Engine e) {
		Controller.e = e;
	}

	public Searcher getS() {
		return s;
	}

	public void setS(Searcher s) {
		Controller.s = s;
	}

	public Result getR() {
		return r;
	}

	public void setR(Result r) {
		Controller.r = r;
	}

}
