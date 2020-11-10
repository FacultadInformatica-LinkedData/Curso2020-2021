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

public class Distrito {

	JFrame frmBusquedaDeDistrito;
	JFrame frmInformacionDetallada;

	/**
	 * Launch the application.
	 */
			public void run() {
				try {
					Distrito window = new Distrito();
					window.frmBusquedaDeDistrito.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 */
	public Distrito() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBusquedaDeDistrito = new JFrame();
		frmBusquedaDeDistrito.getContentPane().setBackground(new Color(125, 192, 138));
		frmBusquedaDeDistrito.setTitle("Informaci\u00F3n de Distrito");
		frmBusquedaDeDistrito.setSize(550, 503);
		frmBusquedaDeDistrito.setLocationRelativeTo(null);
		frmBusquedaDeDistrito.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBusquedaDeDistrito.getContentPane().setLayout(null);
		frmBusquedaDeDistrito.setResizable(false);

		JLabel lblDistrito = new JLabel("Distritos");
		lblDistrito.setFont(new Font("Tahoma", Font.PLAIN, 24));
		lblDistrito.setBounds(220, 95, 324, 66);
		frmBusquedaDeDistrito.getContentPane().add(lblDistrito);

		JLabel lblNombre = new JLabel("Seleccione el distrito sobre la que desea informaci\u00F3n: ");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(60, 150, 450, 30);
		frmBusquedaDeDistrito.getContentPane().add(lblNombre);

		JButton btnAtras = new JButton("Atras");
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Opciones windowOptions = new Opciones();
				frmBusquedaDeDistrito.setVisible(false);
				windowOptions.frameOptions.setVisible(true);
			}
		});
		btnAtras.setBounds(10, 420, 105, 30);
		frmBusquedaDeDistrito.getContentPane().add(btnAtras);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmBusquedaDeDistrito.getContentPane().add(btnExit);



		JComboBox<String> distritos = new JComboBox<String>();
		distritos.setBounds(50, 200, 450, 27);
		frmBusquedaDeDistrito.getContentPane().add(distritos);
		String [] distritos0 = {"Arganzuela", "Barajas", "Carabanchel",
				 "Centro", "Chamartín", "Chamberí", "Ciudad Lineal", "Fuencarral-El Pardo", 
				 "Hortaleza", "Latina" ,"Moncloa-Aravaca", "Moratalaz", "Puente de Vallecas", 
				"Retiro", "Salamanca", "San Blas" ,"Tetuan", "Usera", 
				"Vicalvaro", "Villa de Vallecas", "Villaverde"};
		Arrays.sort(distritos0);
		distritos.setModel(new javax.swing.DefaultComboBoxModel<>(distritos0));
		
		JButton btnBuscar = new JButton("Buscar");
		btnBuscar.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnBuscar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				InformacionDistrito windowInformacionDistrito = new InformacionDistrito((String)distritos.getSelectedItem());
				frmBusquedaDeDistrito.setVisible(false);
				windowInformacionDistrito.frmInformacionDistrito.setVisible(true);
			}
		});
		btnBuscar.setBounds(215, 250, 105, 30);
		frmBusquedaDeDistrito.getContentPane().add(btnBuscar);

		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\Logo-Ayuntamiento-Octb16.png"));
		labelLogo.setBounds(405, 20, 100, 25);
		frmBusquedaDeDistrito.getContentPane().add(labelLogo);
		
	}
}
