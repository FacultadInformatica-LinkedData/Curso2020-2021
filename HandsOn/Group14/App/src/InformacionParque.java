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

public class InformacionParque {

	JFrame frmInformacionParque;
	private JTextField textNombre;
	private JTextArea textEspecie;


	/**
	 * Launch the application.
	 */

			public void run() {
				try {
					InformacionParque window = new InformacionParque("");
					window.frmInformacionParque.setVisible(true);

				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 * @param estacion 
	 */
	public InformacionParque(String parque) {
		initialize(parque);
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize(String parque) {
		// Conexion Base de datos
		ConexionMySQL SQL = new ConexionMySQL();
		Connection conn = SQL.conectarMySQL();

		frmInformacionParque = new JFrame();
		frmInformacionParque.setTitle("Información del parque");
		frmInformacionParque.getContentPane().setBackground(new Color(125, 192, 138));
		frmInformacionParque.setSize(550, 503);
		frmInformacionParque.setLocationRelativeTo(null);
		frmInformacionParque.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmInformacionParque.getContentPane().setLayout(null);
		frmInformacionParque.setResizable(false);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmInformacionParque.getContentPane().add(btnExit);

		JButton btnAtras = new JButton("Atras");
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Parque windowDistrito = new Parque();
				frmInformacionParque.setVisible(false);
				windowDistrito.frmBusquedaDeParque.setVisible(true);

			}
		});
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.setBounds(10, 420, 105, 30);
		frmInformacionParque.getContentPane().add(btnAtras);

		JLabel lblNombre = new JLabel("Parque:");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(10, 45, 324, 66);
		frmInformacionParque.getContentPane().add(lblNombre);

		textNombre = new JTextField();
		textNombre.setBounds(75, 70, 450, 20);
		textNombre.setBackground(new Color(255, 255, 255));
		
		textNombre.setText(parque);

		//		textNombre.setText(xxxx); //Para meter la informacion dentro del cuadro de texto
		frmInformacionParque.getContentPane().add(textNombre);
		textNombre.setColumns(10);
		textNombre.setEditable(false);
		
		JLabel lblEspecie = new JLabel("Listado de especies en el parque seleccionado");
		lblEspecie.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblEspecie.setBounds(90, 120, 400, 30);
		
		
		
		textEspecie = new JTextArea();
		textEspecie.setEditable(false);
		textEspecie.setBounds(70, 150, 400, 250);
		textEspecie.setBackground(new Color(255,255,255));
		textEspecie.setColumns(0);
		frmInformacionParque.getContentPane().add(textEspecie);
		frmInformacionParque.getContentPane().add(lblEspecie);
		
		int unidades=0;	
		String especie="";
		try
		{
			// Query
			String queryEspecie;
			queryEspecie = "SELECT ESPECIE, UNIDADES FROM arboles_y_parques WHERE PARQUE= '" + parque + "' ORDER BY ESPECIE ASC;";
			
			// create the java statement
			Statement st = conn.createStatement();

			// execute the query, and get a java resultset
			ResultSet rs = st.executeQuery(queryEspecie);
			

			// iterate through the java resultset
			
			textEspecie.setText("");
			while (rs.next())
			{
				//METE AQUI LOS DATOSS!!!!!
				especie =rs.getString("ESPECIE");
				unidades = rs.getInt("UNIDADES");
				
				if(especie == " ") {
					textEspecie.setText("Este parque no tiene especies");
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
		frmInformacionParque.getContentPane().add(labelLogo);
	}
}
