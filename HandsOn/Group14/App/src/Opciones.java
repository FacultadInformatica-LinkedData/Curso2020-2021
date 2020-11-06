import java.awt.Color;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.ImageIcon;

public class Opciones {

	JFrame frameOptions;

	/**
	 * Launch the application.
	 */
			public void run() {
				try {
					Opciones window = new Opciones();
					window.frameOptions.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	

	/**
	 * Create the application.
	 */
	public Opciones() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frameOptions = new JFrame();
		frameOptions.setTitle("Options");
		frameOptions.setSize(550, 503);
		frameOptions.setLocationRelativeTo(null);
		frameOptions.getContentPane().setBackground(new Color(125, 192, 138));
		frameOptions.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frameOptions.getContentPane().setLayout(null);
		frameOptions.setResizable(false);

		JLabel lblEspecies = new JLabel("Por especie");
		lblEspecies.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblEspecies.setBounds(75, 165, 358, 33);
		frameOptions.getContentPane().add(lblEspecies);

		JLabel lblOpciones = new JLabel("¿Cómo quiere buscar?");
		lblOpciones.setFont(new Font("Tahoma", Font.PLAIN, 24));
		lblOpciones.setBounds(150, 80, 324, 66);
		frameOptions.getContentPane().add(lblOpciones);

		JLabel lblParque = new JLabel("Por parque");
		lblParque.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblParque.setBounds(225, 165, 358, 33);
		frameOptions.getContentPane().add(lblParque);
		
		JLabel lblDistrito = new JLabel("Por distrito");
		lblDistrito.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblDistrito.setBounds(375, 165, 358, 33);
		frameOptions.getContentPane().add(lblDistrito);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {

			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frameOptions.getContentPane().add(btnExit);

		JButton btnEmpezarBusqueda = new JButton(new ImageIcon("src\\arbol.png"));
		btnEmpezarBusqueda.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnEmpezarBusqueda.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Especie windowEspecie = new Especie();
				frameOptions.setVisible(false);
				windowEspecie.frmBusquedaDeEspecie.setVisible(true);
			}
		});
		btnEmpezarBusqueda.setBounds(65, 200, 113, 113);
		frameOptions.getContentPane().add(btnEmpezarBusqueda);

		JButton btnDistrito = new JButton(new ImageIcon("src\\distritos.jpg"));
		btnDistrito.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnDistrito.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Distrito windowDistrito = new Distrito();
				frameOptions.setVisible(false);
				windowDistrito.frmBusquedaDeDistrito.setVisible(true);
			}
		});
		btnDistrito.setBounds(360, 200, 113, 113);
		frameOptions.getContentPane().add(btnDistrito);
		
		JButton btnParque = new JButton(new ImageIcon("src\\Parque.jpg"));
		btnParque.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnParque.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Parque windowParque = new Parque();
				frameOptions.setVisible(false);
				windowParque.frmBusquedaDeParque.setVisible(true);
			}
		});
		btnParque.setBounds(212, 200, 113, 113);
		frameOptions.getContentPane().add(btnParque);
		
		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\logo-Ayuntamiento-Octb16.png"));
		labelLogo.setBounds(405, 30, 100, 25);
		frameOptions.getContentPane().add(labelLogo);		
	}

}
