import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JSeparator;
import javax.swing.JComboBox;
import java.sql.*;
import java.util.Arrays;
import java.awt.Color;
import javax.swing.ImageIcon;

public class Parque {

	JFrame frmBusquedaDeParque;
	JFrame frmInformacionDetallada;

	/**
	 * Launch the application.
	 */
			public void run() {
				try {
					Parque window = new Parque();
					window.frmBusquedaDeParque.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 */
	public Parque() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBusquedaDeParque = new JFrame();
		frmBusquedaDeParque.getContentPane().setBackground(new Color(125, 192, 138));
		frmBusquedaDeParque.setTitle("Informaci\u00F3n de Parque");
		frmBusquedaDeParque.setSize(550, 503);
		frmBusquedaDeParque.setLocationRelativeTo(null);
		frmBusquedaDeParque.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBusquedaDeParque.getContentPane().setLayout(null);
		frmBusquedaDeParque.setResizable(false);

		JLabel lblParque = new JLabel("Parques");
		lblParque.setFont(new Font("Tahoma", Font.PLAIN, 24));
		lblParque.setBounds(225, 95, 324, 66);
		frmBusquedaDeParque.getContentPane().add(lblParque);

		JLabel lblNombre = new JLabel("Seleccione el parque sobre la que desea informaci\u00F3n: ");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(60, 150, 450, 30);
		frmBusquedaDeParque.getContentPane().add(lblNombre);

		JButton btnAtras = new JButton("Atras");
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Opciones windowOptions = new Opciones();
				frmBusquedaDeParque.setVisible(false);
				windowOptions.frameOptions.setVisible(true);
			}
		});
		btnAtras.setBounds(10, 420, 105, 30);
		frmBusquedaDeParque.getContentPane().add(btnAtras);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmBusquedaDeParque.getContentPane().add(btnExit);



		JComboBox<String> parques = new JComboBox<String>();
		parques.setBounds(50, 200, 450, 27);
		frmBusquedaDeParque.getContentPane().add(parques);
		String [] parques0 = {"CAPRICHO DE LA ALAMEDA DE OSUNA", "CASA DE CAMPO", "CUÑA VERDE DE O´DONNELL Y P. F. FUENTE CARRANTONA", 
				"DEHESA DE LA VILLA", "JARDINES DE SABATINI", "JARDINES DEL BUEN RETIRO", 
				"JARDINES PZA DE ORIENTE-JARDÍN DEL CABO NOVAL-JARDÍN DE LEPANTO", "MADRID RÍO", "PARQUE DEL OESTE- TEMPLO DE DEBOD", 
				"PARQUE FORESTAL VALDEBEBAS", "PARQUE JUAN CARLOS I", "PARQUE JUAN PABLO II", "PARQUE LINEAL DEL MANZANARES",
				"QUINTA DE LOS MOLINOS", "QUINTA FUENTE DEL BERRO", "ROSALEDA DE MADRID (PARQUE DEL OESTE)", "TOTAL", 
				"Z.V.DISTRITO C-LAS TABLAS" };
		Arrays.sort(parques0);
		parques.setModel(new javax.swing.DefaultComboBoxModel<>(parques0));
		
		JButton btnBuscar = new JButton("Buscar");
		btnBuscar.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnBuscar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				InformacionParque windowInformacionDetallada = new InformacionParque((String)parques.getSelectedItem());
				frmBusquedaDeParque.setVisible(false);
				windowInformacionDetallada.frmInformacionParque.setVisible(true);
			}
		});
		btnBuscar.setBounds(215, 250, 105, 30);
		frmBusquedaDeParque.getContentPane().add(btnBuscar);

		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\Logo-Ayuntamiento-Octb16.png"));
		labelLogo.setBounds(405, 20, 100, 25);
		frmBusquedaDeParque.getContentPane().add(labelLogo);
		


	}
}
