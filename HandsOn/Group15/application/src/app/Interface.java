package app;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JPasswordField;
import javax.swing.JSeparator;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;
import java.util.ArrayList;

/**
 * This program demonstrates how to use JPanel in Swing.
 * 
 * @author www.codejava.net
 */
public class Interface extends JFrame {

	private String[] output = new String[2];
	ArrayList<String> centros = new ArrayList<String>();
	ArrayList<String> municipios = new ArrayList<String>();
	private Backend backend = new Backend();

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public Interface() throws IOException {
		super("App");
		this.setResizable(false);

		BufferedImage img = ImageIO.read(new File("resources/madrid.jpg"));
		ImageIcon image = new ImageIcon();
		JLabel imgLabel = new JLabel();
		image.setImage(img);
		imgLabel.setIcon(image);

		// create a new panel with GridBagLayout manager
		JPanel p = new JPanel();
		p.setBackground(Color.white);

		JSeparator s1 = new JSeparator();
		s1.setOrientation(SwingConstants.HORIZONTAL);
		s1.setPreferredSize(new Dimension(0, 15));
		s1.setForeground(Color.white);

		JSeparator s3 = new JSeparator();
		s3.setOrientation(SwingConstants.HORIZONTAL);
		s3.setPreferredSize(new Dimension(0, 15));
		s3.setForeground(Color.white);

		JSeparator s5 = new JSeparator();
		s5.setOrientation(SwingConstants.HORIZONTAL);
		s5.setPreferredSize(new Dimension(0, 15));
		s5.setForeground(Color.white);

		JSeparator s7 = new JSeparator();
		s7.setOrientation(SwingConstants.HORIZONTAL);
		s7.setPreferredSize(new Dimension(0, 15));
		s7.setForeground(Color.white);

		p.setLayout(new BoxLayout(p, BoxLayout.Y_AXIS));

		p.add(imgLabel);

		p.add(s1);

		JLabel label1 = new JLabel("Municipios");
		p.add(label1);

		JComboBox combo1 = new JComboBox();
		municipios = backend.getMunicipality();
		for (int i = 0; i < municipios.size(); i++) {
			combo1.addItem(municipios.get(i));
		}
		p.add(combo1);

		p.add(s3);

		JLabel label2 = new JLabel("Tipo de centro");
		p.add(label2);

		JComboBox combo2 = new JComboBox();
		combo2.addItem("PÚBLICO");
		combo2.addItem("PRIVADO");
		combo2.addItem("PRIVADO CONCERTADO");
		combo2.addItem("PÚBLICO-TITULARIDAD PRIVADA");
		p.add(combo2);

		/*
		 * p.add(s5);
		 * 
		 * JLabel label3 = new JLabel("Número de actividades"); p.add(label3);
		 * 
		 * JComboBox combo3 = new JComboBox(); combo3.addItem("0"); combo3.addItem("1");
		 * combo3.addItem("2 o más"); p.add(combo3);
		 */

		p.add(s7);
		/*
		 * "                                        Buscar colegios                                        "
		 */		
		JButton b = new JButton(
				"Buscar colegios");
		b.setBorder(BorderFactory.createEmptyBorder(10, 65, 10, 65));
		b.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				output[0] = combo1.getSelectedItem().toString();
				output[1] = combo2.getSelectedItem().toString();
				String aux = "";
				centros = backend.execQuery(output);
				for (int i = 0; i < centros.size(); i++) {
					aux = aux +  centros.get(i) + "-";
				}
				JFrame popup = new JFrame();
				popup.add(new JLabel(aux));
				popup.pack();
				popup.setLocation(new Point(960, 540));
				popup.setVisible(true);
			}
		});
		p.add(b);

		// set border for the panel
		p.setBorder(BorderFactory.createEmptyBorder(20, 50, 20, 50));
		add(p);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		pack();
		setLocationRelativeTo(null);
	}

	public static void main(String[] args) {		
		
		// set look and feel to the system look and feel
		try {
			UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
		} catch (Exception ex) {
			ex.printStackTrace();
		}

		SwingUtilities.invokeLater(new Runnable() {
			@Override
			public void run() {
				try {
					new Interface().setVisible(true);
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		});
	}
}
