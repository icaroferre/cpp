from Cocoa import *
from Foundation import NSObject
import sys
import pyperclip

# Main Window
class PaypalCalculatorController(NSWindowController):
    # Bind variables to IB Outlets
    valor = objc.IBOutlet()
    parcelas = objc.IBOutlet()
    counterTextField = objc.IBOutlet()
    valorParcelaTF = objc.IBOutlet()
    valorTaxasTF = objc.IBOutlet()
    stepper = objc.IBOutlet()

    def windowDidLoad(self):
        NSWindowController.windowDidLoad(self)

        # Initial Values
        self.valorTotal = 0.0
        self.stepper.setMaxValue_(12.0)
        self.stepper.setMinValue_(2.0)
        self.stepper.setIntValue_(2)
        self.parcelas.takeIntValueFrom_(self.stepper)
        self.counterTextField.setStringValue_("")
        self.valorParcelaTF.setStringValue_("")
        self.valorTaxasTF.setStringValue_("")
        self.valor.setFloatValue_(100.0)

    # Calculation Method
    @objc.IBAction
    def calculate_(self, sender):
        taxa_paypal = 0.049
        taxa_parcelamento = 0.0239
        taxa_transferencia = 0.6 
        self.valor2 = round(self.valor.floatValue(),2)
        self.parcelas.takeIntValueFrom_(self.stepper)
        parcelas2 = self.parcelas.floatValue()
        self.valorTotal = (self.valor2 + (self.valor2 * taxa_paypal) + taxa_transferencia + (self.valor2 * (parcelas2 * taxa_parcelamento)))
        self.valorTotalDisplay = "R$"+ (format(round(self.valorTotal,4),".2f"))
        self.valorParcela = "R$"+ format(round((self.valorTotal / parcelas2), 2),".2f")
        self.valorTaxas = "R$" + format(round((self.valorTotal - self.valor2), 2),".2f")
        self.updateDisplay()

    # Pyperclip Method (Copiar)
    @objc.IBAction
    def copyValues_(self,sender):
        pyperclip.copy("Valor Inicial: R$" + str(self.valor2) + "\n# de Parcelas: " + str(self.parcelas.intValue()) + "\n-\nValor Total: " + self.valorTotalDisplay + "\nValor por Parcela: " + self.valorParcela + "\nValor de Taxas: " + self.valorTaxas)

    @objc.IBAction
    def stepperChanged_(self,sender):
        self.parcelas.takeIntValueFrom_(self.stepper)

    # Update Stepper value when the Parcelas texfield has been manually changed
    @objc.IBAction
    def parcelasChanged_(self,sender):
        self.stepper.takeIntValueFrom_(self.parcelas)
        self.calculate_(sender)

    # Updates the Display / Textfields
    def updateDisplay(self):
        self.counterTextField.setStringValue_(self.valorTotalDisplay)
        self.valorParcelaTF.setStringValue_(self.valorParcela)
        self.valorTaxasTF.setStringValue_(self.valorTaxas)


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    
    # Initiate the contrller with a XIB
    viewController = PaypalCalculatorController.alloc().initWithWindowNibName_("MainMenu")

    # Show the window
    viewController.showWindow_(viewController)

    # Bring app to top
    NSApp.activateIgnoringOtherApps_(True)
    
    from PyObjCTools import AppHelper
    AppHelper.runEventLoop()

sys.exit(NSApplicationMain(sys.argv))
