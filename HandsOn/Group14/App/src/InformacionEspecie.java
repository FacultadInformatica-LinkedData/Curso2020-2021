import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.awt.event.ActionEvent;
import java.awt.Font;
import java.awt.Point;

import javax.swing.JTextField;
import javax.swing.ScrollPaneConstants;
import javax.swing.ImageIcon;

public class InformacionEspecie {

	JFrame frmInformacionEspecie;
	private JTextField textNombre;
	private JTextField textUnidades;
	private JTextArea textParque;
	private JTextArea textDistrito;

	/**
	 * Launch the application.
	 */

			public void run() {
				try {
					InformacionEspecie window = new InformacionEspecie("");
					window.frmInformacionEspecie.setVisible(true);

				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 * @param estacion 
	 */
	public InformacionEspecie(String especie) {
		initialize(especie);
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize(String especie) {
		// Conexion Base de datos
		ConexionMySQL SQL = new ConexionMySQL();
		Connection conn = SQL.conectarMySQL();

		frmInformacionEspecie = new JFrame();
		frmInformacionEspecie.setTitle("Información de la especie");
		frmInformacionEspecie.getContentPane().setBackground(new Color(125, 192, 138));
		frmInformacionEspecie.setSize(550, 503);
		frmInformacionEspecie.setLocationRelativeTo(null);
		frmInformacionEspecie.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmInformacionEspecie.getContentPane().setLayout(null);
		frmInformacionEspecie.setResizable(false);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmInformacionEspecie.getContentPane().add(btnExit);

		JButton btnAtras = new JButton("Atras");
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Especie windowEspecie = new Especie();
				frmInformacionEspecie.setVisible(false);
				windowEspecie.frmBusquedaDeEspecie.setVisible(true);

			}
		});
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.setBounds(10, 420, 105, 30);
		frmInformacionEspecie.getContentPane().add(btnAtras);

		JLabel lblNombre = new JLabel("Especie:");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(100, 45, 324, 66);
		frmInformacionEspecie.getContentPane().add(lblNombre);

		textNombre = new JTextField();
		textNombre.setBounds(170, 70, 260, 20);
		textNombre.setBackground(new Color(255, 255, 255));
		
		textNombre.setText(especie);

		//		textNombre.setText(xxxx); //Para meter la informacion dentro del cuadro de texto
		frmInformacionEspecie.getContentPane().add(textNombre);
		textNombre.setColumns(10);
		textNombre.setEditable(false);
		
		JLabel lblParque = new JLabel("Listado de parques con la especie seleccionada");
		lblParque.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblParque.setBounds(90, 100, 400, 30);
		
		
		
		textParque = new JTextArea();
		textParque.setBackground(new Color(255,255,255));
		textParque.setEditable(false);
		JScrollPane scroll = new JScrollPane(textParque);
		scroll.setBounds(30, 130, 470, 120);
		frmInformacionEspecie.getContentPane().add(scroll);	
		frmInformacionEspecie.getContentPane().add(lblParque);
		
		
		JLabel lblDistrito = new JLabel("Listado de distritos con la especie seleccionada");
		lblDistrito.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblDistrito.setBounds(90, 260, 400, 30);
		
		textDistrito = new JTextArea();
		//textDistrito.setBounds(30, 290, 500, 120);
		textDistrito.setBackground(new Color(255,255,255));
		JScrollPane scrollDistrito = new JScrollPane(textDistrito);
		scrollDistrito.setBounds(30, 290, 470, 120);
		frmInformacionEspecie.getContentPane().add(scrollDistrito);
		frmInformacionEspecie.getContentPane().add(lblDistrito);
		int unidades=0;	
		String parque="";
		try
		{
			// Query
			String queryParque;
			queryParque = "SELECT PARQUE, UNIDADES FROM arboles_y_parques WHERE ESPECIE= '" + especie + "' ORDER BY PARQUE ASC;";
			
			// create the java statement
			Statement st = conn.createStatement();

			// execute the query, and get a java resultset
			ResultSet rs = st.executeQuery(queryParque);
			

			// iterate through the java resultset
			
			textParque.setText("");
			while (rs.next())
			{
				//METE AQUI LOS DATOSS!!!!!
				parque =rs.getString("PARQUE");
				unidades = rs.getInt("UNIDADES");
				
				if(parque == " ") {
					textParque.setText("La especie seleccionada no se encuentra en ningun parque");
				}
				else {
					textParque.append(parque + ". UNIDADES: "+ unidades +'\n');
				}
					
				
			}
			st.close();
		}
		catch (Exception e)
		{
			System.err.println("Got an exception! ");
			System.err.println(e.getMessage());
		}
		
		String distritos = "";
		int cantidad = 0;
		
		try
		{
			// Query
			String queryDistrito = "";
			queryDistrito = "SELECT Nombre_distrito, Unidades FROM arboles_y_distritos WHERE NOMBRE_ESPECIE= '" + especie + "' ORDER BY Nombre_distrito ASC;";
			
			// create the java statement
			Statement st = conn.createStatement();

			// execute the query, and get a java resultset
			ResultSet rs = st.executeQuery(queryDistrito);

			// iterate through the java resultset
			
			textDistrito.setText("");
			while (rs.next())
			{
				//METE AQUI LOS DATOSS!!!!!
				distritos =rs.getString("Nombre_distrito");
				cantidad = rs.getInt("Unidades");
	
				if(parque == " ") {
					textDistrito.setText("La especie seleccionada no se encuentra en ningun parque");
				}
				else {
					textDistrito.append(distritos + ". UNIDADES: "+ cantidad + '\n');
				}
				
				
			}
			st.close();
		}
		catch (Exception e)
		{
			System.err.println("Got an exception! ");
			System.err.println(e.getMessage());
		}
		
		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\Logo-Ayuntamiento-Octb16.png"));
		labelLogo.setBounds(405, 20, 100, 25);
		frmInformacionEspecie.getContentPane().add(labelLogo);
	}
}
