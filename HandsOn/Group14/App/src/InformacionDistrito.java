import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.JComboBox;

import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Arrays;
import java.awt.event.ActionEvent;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.ImageIcon;

public class InformacionDistrito {

	JFrame frmInformacionDistrito;
	private JTextField textNombre;
	private JTextArea textEspecie;


	/**
	 * Launch the application.
	 */

			public void run() {
				try {
					InformacionDistrito window = new InformacionDistrito("");
					window.frmInformacionDistrito.setVisible(true);

				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 * @param estacion 
	 */
	public InformacionDistrito(String distrito) {
		initialize(distrito);
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize(String distrito) {
		// Conexion Base de datos
		ConexionMySQL SQL = new ConexionMySQL();
		Connection conn = SQL.conectarMySQL();

		frmInformacionDistrito = new JFrame();
		frmInformacionDistrito.setTitle("Información del distrito");
		frmInformacionDistrito.getContentPane().setBackground(new Color(125, 192, 138));
		frmInformacionDistrito.setSize(550, 503);
		frmInformacionDistrito.setLocationRelativeTo(null);
		frmInformacionDistrito.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmInformacionDistrito.getContentPane().setLayout(null);
		frmInformacionDistrito.setResizable(false);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmInformacionDistrito.getContentPane().add(btnExit);

		JButton btnAtras = new JButton("Atras");
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Distrito windowDistrito = new Distrito();
				frmInformacionDistrito.setVisible(false);
				windowDistrito.frmBusquedaDeDistrito.setVisible(true);

			}
		});
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.setBounds(10, 420, 105, 30);
		frmInformacionDistrito.getContentPane().add(btnAtras);

		JLabel lblNombre = new JLabel("Distrito:");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(100, 45, 324, 66);
		frmInformacionDistrito.getContentPane().add(lblNombre);

		textNombre = new JTextField();
		textNombre.setBounds(170, 70, 260, 20);
		textNombre.setBackground(new Color(255, 255, 255));
		
		textNombre.setText(distrito);

		//		textNombre.setText(xxxx); //Para meter la informacion dentro del cuadro de texto
		frmInformacionDistrito.getContentPane().add(textNombre);
		textNombre.setColumns(10);
		textNombre.setEditable(false);
		
		JLabel lblEspecie = new JLabel("Listado de especies en el distrito seleccionado");
		lblEspecie.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblEspecie.setBounds(90, 120, 400, 30);
		
		
		
		textEspecie = new JTextArea();
		textEspecie.setBounds(70, 150, 400, 250);
		textEspecie.setBackground(new Color(255,255,255));
		textEspecie.setColumns(0);
		textEspecie.setEditable(false);
		frmInformacionDistrito.getContentPane().add(textEspecie);
		frmInformacionDistrito.getContentPane().add(lblEspecie);
		
		int unidades=0;	
		String especie="";
		try
		{
			// Query
			String queryEspecie;
			queryEspecie = "SELECT NOMBRE_ESPECIE, Unidades FROM arboles_y_distritos WHERE Nombre_distrito= '" + distrito + "' ORDER BY NOMBRE_ESPECIE ASC;";
			
			// create the java statement
			Statement st = conn.createStatement();

			// execute the query, and get a java resultset
			ResultSet rs = st.executeQuery(queryEspecie);
			

			// iterate through the java resultset
			
			textEspecie.setText("");
			while (rs.next())
			{
				//METE AQUI LOS DATOSS!!!!!
				especie =rs.getString("NOMBRE_ESPECIE");
				unidades = rs.getInt("UNIDADES");
				
				if(especie == " ") {
					textEspecie.setText("Este distrito no tiene especies");
				}
				else {
					textEspecie.append(especie + ". UNIDADES: "+ unidades +'\n');
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
		frmInformacionDistrito.getContentPane().add(labelLogo);
	}
}
