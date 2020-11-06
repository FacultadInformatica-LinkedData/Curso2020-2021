package app;

import java.awt.EventQueue;


import javax.swing.JFrame;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JLabel;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import com.jgoodies.forms.layout.FormLayout;
import com.jgoodies.forms.layout.ColumnSpec;
import com.jgoodies.forms.layout.RowSpec;
import java.awt.BorderLayout;
import java.awt.Color;

import javax.swing.ImageIcon;
import javax.swing.SwingConstants;
import javax.swing.LayoutStyle.ComponentPlacement;
import com.sun.awt.*;



public class Ejecucion {

	public static void main(String[] args) throws InterruptedException {
		
		Splash splash =  new Splash();
		splash.getFrame().setVisible(true);
		
		try {
			Thread.sleep(1000);
			MainScreen mainScreen = new MainScreen();
			splash.getFrame().dispose();
			
			mainScreen.getFrame().setLocationRelativeTo(null);

			mainScreen.getFrame().setVisible(true);
			
		}
		catch(Exception e) {
			
		}
		
		
	}
	
	
	
}
