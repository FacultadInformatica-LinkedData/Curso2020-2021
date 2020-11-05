import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import java.awt.Font;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.ImageIcon;

public class Inicio {

	JFrame frmInicio;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable(){
			public void run() {
				try {
					Inicio windowIndex = new Inicio();
					windowIndex.frmInicio.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Inicio() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmInicio = new JFrame();	
		frmInicio.setTitle("Inicio");
		frmInicio.setSize(550, 503);
		frmInicio.setLocationRelativeTo(null);
		frmInicio.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmInicio.getContentPane().setLayout(null);
		frmInicio.setResizable(false); //Para no poder maximizar

		JButton btnEmpezar = new JButton("Comenzar");
		btnEmpezar.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnEmpezar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Opciones windowOptions = new Opciones();
				frmInicio.setVisible(false);
				windowOptions.frameOptions.setVisible(true);

			}
		});
		btnEmpezar.setBounds(200, 400, 129, 40);
		frmInicio.getContentPane().add(btnEmpezar);

		JLabel lblBienvenido = new JLabel("Bienvenido a MadTrees");
		lblBienvenido.setFont(new Font("Tahoma", Font.BOLD, 24));
		lblBienvenido.setBounds(130, 45, 324, 66);
		frmInicio.getContentPane().add(lblBienvenido);
		
		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\Logo-Ayuntamiento-Octb16.png"));
		labelLogo.setBounds(405, 20, 100, 25);
		frmInicio.getContentPane().add(labelLogo);
		
		JLabel labelInicio = new JLabel("");
		labelInicio.setIcon(new ImageIcon("src\\Madrid4.jpg"));
		labelInicio.setSize(550, 503);
		frmInicio.getContentPane().add(labelInicio);
	}

}
