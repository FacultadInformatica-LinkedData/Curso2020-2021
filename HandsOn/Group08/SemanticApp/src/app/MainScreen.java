package app;

import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.image.ImageObserver;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;

import net.miginfocom.swing.MigLayout;
import javax.swing.BoxLayout;
import javax.swing.DefaultListModel;
import javax.swing.GroupLayout;
import javax.swing.ImageIcon;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JComboBox;
import javax.swing.JTable;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JButton;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.JTableHeader;
import javax.swing.table.TableColumnModel;

import com.teamdev.jxbrowser.browser.Browser;
import com.teamdev.jxbrowser.engine.Engine;
import com.teamdev.jxbrowser.engine.EngineOptions;
import com.teamdev.jxbrowser.view.swing.BrowserView;

import static com.teamdev.jxbrowser.engine.RenderingMode.HARDWARE_ACCELERATED;

import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;

import java.awt.Font;
import javax.swing.table.DefaultTableModel;
import javax.swing.JPanel;
import java.awt.Toolkit;


public class MainScreen {
	
	public Queries querie;

	private ArrayList<String> calles;
	private ArrayList<String> callesAux;
	private ArrayList<String> distritos;
	private ArrayList<String> conectores;
	private DefaultListModel<String> model;
	
	private ArrayList<PuntoRecarga> auxList;

	private JFrame frame;
	private JTable table;
	private JComboBox<String> distritos_1;
	private JComboBox<String> calles_1;
	private JComboBox<String> conectores_1;
	private JList list;
	private JPanel panel;
	
	private Browser browser;
	
	

	public JFrame getFrame() {
		return frame;
	}

	
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MainScreen window = new MainScreen();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public MainScreen() {
		
		querie = new Queries();
		distritos = querie.getDistritos();
		calles = querie.getCalles();
		conectores = querie.getConectores();
		
		initialize();

		
		System.setProperty("jxbrowser.license.key", "1BNDHFSC1FX6PUG41DO53BC8HMZIFEP1JPJG0Z8IDTUI51IS4MSFRBDUHQ4JCDK3JIB8PV");

		// Creating and running Chromium engine
		EngineOptions options =
				EngineOptions.newBuilder(HARDWARE_ACCELERATED).build();
		Engine engine = Engine.newInstance(options);
		browser = engine.newBrowser();

		SwingUtilities.invokeLater(() -> {
			// Creating Swing component for rendering web content
			// loaded in the given Browser instance.
			BrowserView view = BrowserView.newInstance(browser);

			// Creating and displaying Swing app frame.
			// Close Engine and onClose app window
			frame.addWindowListener(new WindowAdapter() {
				@Override
				public void windowClosing(WindowEvent e) {
					engine.close();
				}
			});
			frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
			JTextField addressBar = new JTextField("https://maps.google.es/maps?hl=es&tab=rl");
			addressBar.addActionListener(e ->
			browser.navigation().loadUrl(addressBar.getText()));
			view.setSize(650, 611);
			//            panel.add(addressBar, BorderLayout.NORTH);
			panel.add(view, BorderLayout.CENTER);


			browser.navigation().loadUrl(addressBar.getText());
		});
		
//		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		
		frame.setBounds(100, 100, 1341, 910);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				
		String[] columnNames = {"Distrito", "Calle", "Edificio", "Conector", "Potencia", "Terminal", "CoordX", "CoordY"};

        Object[][] data = {
        		{"", "", "", "", new Integer(0),new Integer(0), new Double(0), new Double(0)}
        };
		
		table = new JTable(data,columnNames);
		table.setModel(new DefaultTableModel(
			new Object[][] {
				{"", "", "", "", new Integer(0), new Integer(0), new Double(0.0), new Double(0.0)},
			},
			new String[] {
				"Distrito", "Calle", "Edificio", "Conector", "Potencia", "Terminal", "CoordX", "CoordY"
			}
		));
//		table.getColumnModel().getColumn(0).setPreferredWidth(40);
//		table.getColumnModel().getColumn(1).setPreferredWidth(15);
//		table.getColumnModel().getColumn(2).setPreferredWidth(5);
//		table.getColumnModel().getColumn(3).setPreferredWidth(5);
//		table.getColumnModel().getColumn(4).setPreferredWidth(15);
		table.getColumnModel().getColumn(0).setMaxWidth(150);
		table.getColumnModel().getColumn(0).setMinWidth(150);
		table.getColumnModel().getColumn(0).setPreferredWidth(150);
		table.getColumnModel().getColumn(4).setMaxWidth(130);
		table.getColumnModel().getColumn(4).setMinWidth(130);
		table.getColumnModel().getColumn(4).setPreferredWidth(130);
		table.getColumnModel().getColumn(5).setMaxWidth(70);
		table.getColumnModel().getColumn(5).setMinWidth(70);
		table.getColumnModel().getColumn(5).setPreferredWidth(70);
		table.getColumnModel().getColumn(6).setMaxWidth(85);
		table.getColumnModel().getColumn(6).setMinWidth(85);
		table.getColumnModel().getColumn(6).setPreferredWidth(85);
		table.getColumnModel().getColumn(7).setMaxWidth(85);
		table.getColumnModel().getColumn(7).setMinWidth(85);
		table.getColumnModel().getColumn(7).setPreferredWidth(85);
		table.setEnabled(false);
		table.setRowHeight(46);
		
		DefaultTableCellRenderer centerRenderer = new DefaultTableCellRenderer();
		centerRenderer.setHorizontalAlignment( JLabel.CENTER );
		
		 for(int x=0;x<table.getColumnCount();x++){
	            table.getColumnModel().getColumn(x).setCellRenderer( centerRenderer );
	           }
//	    columnModel.getColumn(3).setPreferredWidth();
//	    columnModel.getColumn(3).setPreferredWidth();
 		
		JTableHeader header = table.getTableHeader();
		
        header.setBorder(javax.swing.BorderFactory.createMatteBorder(0, 0, 1, 1, new java.awt.Color(255, 255, 255)));

		
		header.setBackground(new Color(65,65,65));
	    header.setForeground(Color.white);
		
	    JScrollPane scroll = new JScrollPane(table);
	    
	    distritos_1 = new JComboBox<String>();
	    distritos_1.setFont(new Font("Segoe UI Light", Font.PLAIN, 16));
	    	
		calles_1 = new JComboBox<String>();
		calles_1.setFont(new Font("Segoe UI Light", Font.PLAIN, 16));
		
		conectores_1 = new JComboBox<String>();		
		conectores_1.setFont(new Font("Segoe UI Light", Font.PLAIN, 16));
		
		distritos_1.addItem("Seleccione un distrito");
		calles_1.addItem("Seleccione una calle");
		conectores_1.addItem("Seleccione un conector");

		for(int i=0; i<distritos.size(); i++) {
			distritos_1.addItem(distritos.get(i));
		}

		for(int i=0; i<calles.size(); i++) {
			calles_1.addItem(calles.get(i));
		}

		for(int i=0; i<conectores.size(); i++) {
			conectores_1.addItem(conectores.get(i));
		}
		
		
		JButton btnNewButton = new JButton("Search");
		btnNewButton.setFont(new Font("Segoe UI Light", Font.PLAIN, 18));
		
		list = new JList();
		list.setFont(new Font("Segoe UI Historic", Font.PLAIN, 14));

	    JScrollPane sp = new JScrollPane(list);
		
		panel = new JPanel();
	
		GroupLayout groupLayout = new GroupLayout(frame.getContentPane());
		groupLayout.setHorizontalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addContainerGap()
					.addGroup(groupLayout.createParallelGroup(Alignment.LEADING)
						.addGroup(Alignment.TRAILING, groupLayout.createSequentialGroup()
							.addComponent(distritos_1, GroupLayout.PREFERRED_SIZE, 238, GroupLayout.PREFERRED_SIZE)
							.addGap(60)
							.addComponent(calles_1, GroupLayout.PREFERRED_SIZE, 362, GroupLayout.PREFERRED_SIZE)
							.addPreferredGap(ComponentPlacement.RELATED, 89, Short.MAX_VALUE)
							.addComponent(conectores_1, GroupLayout.PREFERRED_SIZE, 316, GroupLayout.PREFERRED_SIZE)
							.addGap(55)
							.addComponent(btnNewButton, GroupLayout.PREFERRED_SIZE, 185, GroupLayout.PREFERRED_SIZE))
						.addGroup(groupLayout.createSequentialGroup()
							.addComponent(sp, GroupLayout.PREFERRED_SIZE, 453, GroupLayout.PREFERRED_SIZE)
							.addGap(296)
							.addComponent(panel, GroupLayout.PREFERRED_SIZE, 302, GroupLayout.PREFERRED_SIZE))
						.addComponent(scroll, Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 1305, Short.MAX_VALUE))
					.addContainerGap())
		);
		groupLayout.setVerticalGroup(
			groupLayout.createParallelGroup(Alignment.LEADING)
				.addGroup(groupLayout.createSequentialGroup()
					.addContainerGap()
					.addGroup(groupLayout.createParallelGroup(Alignment.LEADING, false)
						.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
							.addComponent(conectores_1, GroupLayout.DEFAULT_SIZE, 47, Short.MAX_VALUE)
							.addComponent(btnNewButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
						.addGroup(groupLayout.createParallelGroup(Alignment.BASELINE)
							.addComponent(distritos_1, GroupLayout.DEFAULT_SIZE, 47, Short.MAX_VALUE)
							.addComponent(calles_1, GroupLayout.DEFAULT_SIZE, 47, Short.MAX_VALUE)))
					.addGap(60)
					.addComponent(scroll, GroupLayout.PREFERRED_SIZE, 69, GroupLayout.PREFERRED_SIZE)
					.addGroup(groupLayout.createParallelGroup(Alignment.LEADING)
						.addGroup(groupLayout.createSequentialGroup()
							.addGap(65)
							.addComponent(panel, GroupLayout.PREFERRED_SIZE, 218, GroupLayout.PREFERRED_SIZE))
						.addGroup(groupLayout.createSequentialGroup()
							.addGap(73)
							.addComponent(sp, GroupLayout.PREFERRED_SIZE, 600, GroupLayout.PREFERRED_SIZE)))
					.addContainerGap())
		);
		
		distritos_1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				
				if(distritos_1.getSelectedIndex()!=-1 && distritos_1.getSelectedIndex()!=0) {
									
					callesAux = querie.calles(distritos_1.getSelectedItem().toString());
					calles_1.removeAllItems();
					calles_1.addItem("Seleccione una calle");

					for(int i=0; i<callesAux.size(); i++) {
						calles_1.addItem(callesAux.get(i));
					}
				}
				else if(distritos_1.getSelectedIndex()==0) {
					
					calles_1.removeAllItems();
					calles_1.addItem("Seleccione una calle");

					for(int i=0; i<calles.size(); i++) {
						calles_1.addItem(calles.get(i));
					}
				}
			}
		});
		
		btnNewButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String distrito = "";
				String calle = "";
				String conector = "";
				
				auxList = new ArrayList<PuntoRecarga>();
				
				if(distritos_1.getSelectedIndex()>0) {
					distrito = distritos_1.getSelectedItem().toString();
				}
				if(calles_1.getSelectedIndex()>0) {
					calle = calles_1.getSelectedItem().toString();
				}
				if(conectores_1.getSelectedIndex()>0) {
					conector = conectores_1.getSelectedItem().toString();
				}
				
				if(calle.equals("") && conector.equals("")) {	
					auxList = querie.busquedaDistrito(distrito);					
				}
				
				else if(distrito.equals("") && calle.equals("")) {
					auxList = querie.busquedaConector(conector);					
				}
				
				else if(conector.equals("")) {					
					auxList = querie.busquedaCalle(calle);					
				}
	
				else if(distrito.contentEquals("")){
					auxList = querie.busquedaCalleConector(calle, conector);
				}
				else if(calle.equals("")) {
					auxList = querie.busquedaDistritoConector(distrito, conector);
				}
				else {
					System.out.println("3 cosas");
					auxList = querie.busquedaDistritoCalleConector(distrito, calle, conector);
					System.out.println("size " + auxList.size());
				}
				
				model = new DefaultListModel<String>();			
				
				model.removeAllElements();
				
//				System.out.println("checking " + auxList);
				
				if(auxList !=null && auxList.size()!=0) {
					for(int i = 0; i<auxList.size(); i++) {
						PuntoRecarga elem = auxList.get(i);
						String aux = elem.getDistrito() + " - " + elem.getCalle() + " - " + elem.getConector();
						model.addElement(aux);
					}
				}
				else {
					JOptionPane.showMessageDialog(null, "No se encuentra ningún punto de recarga con esas características");
				}			
				
				list.setModel(model);
				
			}
		});
		
		list.addMouseListener(new MouseAdapter(){
	          @Override
	          public void mouseClicked(MouseEvent e) {
	              System.out.println("Mouse click.");
	              int index = list.getSelectedIndex();
	              System.out.println("Index Selected: " + index);
	              String s = (String) list.getSelectedValue();
	              System.out.println("Value Selected: " + s.toString());
	              
	              PuntoRecarga auxPC = auxList.get(index);
	              
	              table.setValueAt(auxPC.getDistrito(), 0, 0);
	              table.setValueAt(auxPC.getCalle(), 0, 1);
	              table.setValueAt(auxPC.getEdificio(), 0, 2);
	              table.setValueAt(auxPC.getConector(), 0, 3);
	              table.setValueAt(auxPC.getPotencia(), 0, 4);
	              table.setValueAt(auxPC.getTerminal(), 0, 5);
	              table.setValueAt(auxPC.getCoordX(), 0, 6);
	              table.setValueAt(auxPC.getCoordY(), 0, 7);
	              

	          }
	    });
		
		
		
		frame.getContentPane().setLayout(groupLayout);
	}
}
