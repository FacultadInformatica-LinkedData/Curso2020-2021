import java.sql.Connection;

import java.sql.DriverManager;
import java.sql.SQLException;

//Clase que utilizaremos para realirzar la conexion con la BD
public class ConexionMySQL {

	public String driver = "com.mysql.jdbc.Driver";
	public String database = "semantic_web";
	public String hostname = "localhost";
	public String port = "3306";
	public String url = "jdbc:mysql://" + hostname + ":" + port + "/" + database + "?useSSL=false";
	public String username = "root";
	public String password = "root";

	public Connection conectarMySQL() {
		Connection conn = null;

		try {
			Class.forName(driver);
			conn = (Connection) DriverManager.getConnection(url, username, password);
			System.out.println("Conexion aceptada");
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
		
		return conn;
	}

}