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

public class Especie {

	JFrame frmBusquedaDeEspecie;
	JFrame frmInformacionDetallada;

	/**
	 * Launch the application.
	 */

			public void run() {
				try {
					Especie window = new Especie();
					window.frmBusquedaDeEspecie.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

	/**
	 * Create the application.
	 */
	public Especie() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frmBusquedaDeEspecie = new JFrame();
		frmBusquedaDeEspecie.getContentPane().setBackground(new Color(125, 192, 138));
		frmBusquedaDeEspecie.setTitle("Informaci\u00F3n de Especie");
		frmBusquedaDeEspecie.setSize(550, 503);
		frmBusquedaDeEspecie.setLocationRelativeTo(null);
		frmBusquedaDeEspecie.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frmBusquedaDeEspecie.getContentPane().setLayout(null);
		frmBusquedaDeEspecie.setResizable(false);

		JLabel lblEspecie = new JLabel("Especies");
		lblEspecie.setFont(new Font("Tahoma", Font.PLAIN, 24));
		lblEspecie.setBounds(225, 95, 324, 66);
		frmBusquedaDeEspecie.getContentPane().add(lblEspecie);

		JLabel lblNombre = new JLabel("Seleccione la especie sobre la que desea informaci\u00F3n: ");
		lblNombre.setFont(new Font("Tahoma", Font.PLAIN, 18));
		lblNombre.setBounds(60, 150, 450, 30);
		frmBusquedaDeEspecie.getContentPane().add(lblNombre);

		JButton btnAtras = new JButton("Atras");
		btnAtras.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnAtras.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				Opciones windowOptions = new Opciones();
				frmBusquedaDeEspecie.setVisible(false);
				windowOptions.frameOptions.setVisible(true);
			}
		});
		btnAtras.setBounds(10, 420, 105, 30);
		frmBusquedaDeEspecie.getContentPane().add(btnAtras);

		JButton btnExit = new JButton("Salir");
		btnExit.setFont(new Font("Tahoma", Font.BOLD, 13));
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setBounds(420, 420, 105, 30);
		frmBusquedaDeEspecie.getContentPane().add(btnExit);



		JComboBox<String> especies = new JComboBox<String>();
		especies.setBounds(50, 200, 450, 27);
		frmBusquedaDeEspecie.getContentPane().add(especies);
		String [] especies0 = {"Abies nordmanniana", "Acacia dealbata", "Acer campestre", "Acer negundo", "Acer pseudoplatanus", "Acer x freemanii (Arce)", "Aesculus hippocastanum", 
				"Ailanthus altissima", "Betula utilis", "Catalpa bignonioides", "Cedrus atlantica", "Cedrus deodara", "Cedrus libani", "Cedrus atlantica 'Glauca'","Celtis australis", 
				"Cercis siliquastrum", "Cupressocyparis leylandii","Cupressus arizonica", "Cupressus macrocarpa", 
				"Cupressus sempervirens", "Cupressus x leylandii", "Eucalyptus sp", "Fraxinus angustifolia", "Fraxinus excelsior", "Ginkgo biloba",
				"Gleditsia triacanthos", "Gleditsia triacanthos inermes", "Judas tree", "Koelreuteria paniculata", "Ligustrum japonicum", "Ligustrum lucidum", 
				"Liquidambar styraciflua", "Magnolia grandiflora", "Melia azedarach", "Morus alba", "Olea europaea", "Otros", "Pinus halepensis",
				"Pinus pinea", "Platanus hybrida", "Platanus orientalis", "Platanus X hispanica", "Populus alba", "Populus nigra", "Populus nigra var. Italica",
				"Populus X canadensis", "Prunus amygdalus", "Prunus cerasifera", "Prunus cerasifera var. pissardii", "Prunus dulcis", "Punica granatum", 
				"Pyrus calleryana", "Quercus ilex", "Quercus robur", "Robinia pseudoacacia", "Sophora japonica", "Taxus baccata", "Thuja occidentalis", "Tilia platyphyllos", 
				"Trachycarpus fortunei", "Ulmuns minor", "Ulmus pumila", "Ulmus sp."};
		Arrays.sort(especies0);
		especies.setModel(new javax.swing.DefaultComboBoxModel<>(especies0));
		
		JButton btnBuscar = new JButton("Buscar");
		btnBuscar.setFont(new Font("Tahoma", Font.BOLD, 12));
		btnBuscar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				InformacionEspecie windowInformacionEspecie = new InformacionEspecie((String)especies.getSelectedItem());
				frmBusquedaDeEspecie.setVisible(false);
				windowInformacionEspecie.frmInformacionEspecie.setVisible(true);
			}
		});
		btnBuscar.setBounds(215, 250, 105, 30);
		frmBusquedaDeEspecie.getContentPane().add(btnBuscar);

		JLabel labelLogo = new JLabel("");
		labelLogo.setIcon(new ImageIcon("src\\logo-Ayuntamiento-Octb16.jpg"));
		labelLogo.setBounds(405, 20, 100, 25);
		frmBusquedaDeEspecie.getContentPane().add(labelLogo);
	

	}
}
