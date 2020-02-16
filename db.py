from cours import cours
from etudiant import etudiant
from note import note
from functools import reduce
class db:
    def __init__(self, listeEtudiant=[], listeCour=[], listeNote=[]):
        self.liste_etudiants = listeEtudiant
        self.liste_cours = listeCour
        self.liste_notes = listeNote
    def ajouterEtudiant(self,etudiant):
        self.liste_etudiants.append(etudiant)
    def supprimerEudiant(self, etudiant):
        self.liste_etudiants.remove(etudiant)
    def editerEtudiant(self, etudiant, nouveauPrenomEtudiant=None,nouveauNomEtudiant=None,nouveauNiveauEtudiant=None):
        self.supprimerEudiant(etudiant)
        if nouveauPrenomEtudiant is not None:
          etudiant.prenom_etudiant=nouveauPrenomEtudiant
        if nouveauNomEtudiant is not None:
          etudiant.nom_etudiant=nouveauNomEtudiant
        if nouveauNiveauEtudiant is not None:
          etudiant.niveau_etudiant=nouveauNiveauEtudiant
        self.ajouterEtudiant(etudiant)
        return etudiant
    def ajouterCour(self,cours):
        self.liste_cours.append(cours)
    def supprimerCours(self,cours):
        self.liste_cours.remove(cours)

    def editerCours(self,nouIntCours=None,nouNivCours=None):
        self.supprimerCours(cours)
        if nouIntCours is not None:
           self.intitule_cours=nouIntCours
           self.niveau_cours=nouNivCours
    def ajouterNote(self,note):
        self.liste_notes.append(note)
    def supprimerNote(self,note):
        self.liste_notes.remove(note)
    def editerNote(self, note, nouvelle_note=None):
        self.supprimerNote(note)
        if nouvelle_note is not None:
           note.note=nouvelle_note
           self.ajouterNote(note)
           return note
    def calcMoyenneImperatif(self,note):
        noteCours=self.noteCoursImp(note)
        return sum(noteCours)/len(noteCours)
    def noteCoursImp(self,cours):
        noteCours=[]
        for cour in self.liste_notes:
            if cour.code_cours==cours:
               noteCours.append(cour.cour)
        return noteCours
    def calcMoyenneEtudiantImp(self,etudiant):
       noteEtudiant=self.noteEtudiantImp(etudiant)
       return sum(noteEtudiant)/len(noteEtudiant)
    def noteEtudiantImp(self,etudiant):
        noteEtu=[]
        for notes in self.liste_etudiants:
            if notes.numero_etudiant==etudiant.numero_etudiant:
               noteEtu.append(notes.notes)
        return noteEtu
    def moyenneCoursFilter_Map_Reduce(self,cours):
        moy=self(cours)
        moyCours=reduce(lambda a,b:a+b,moy)/len(moy)
        notes=list(filter(lambda note:note.code_cours==moyCours.code_cours,self.liste_notes))
        valNote=list(map(lambda note:note.note,notes))
        return valNote
    def moyenneEtudiantFilter_Map_Reduce(self,etudiant):
        moy=self(etudiant)
        moyEtu=reduce(lambda a,b:a+b,moy)/len(moy)
        notes=list(filter(lambda note:note.numero_etudiant==moyEtu.numero_etudiant,self.liste_notes))
        valNote=list(map(lambda note:note.note,notes))
        return valNote
if __name__ == '__main__':
        dataBase=db()
        etudiantUn=etudiant(1,"x","y","faible")
        etudiantDeux = etudiant(1, "a", "z", "eleve")
        dataBase.ajouterEtudiant(etudiantUn)
        dataBase.ajouterEtudiant(etudiantDeux)
        coursUn = cours('1', 'NFP121', '3')
        coursDeux = cours('2', 'MVA005', '1')
        db.ajouterCour(coursUn)
        db.ajouterCour(coursDeux)
        db.ajouterCour(note(1, '1', 9))
        db.ajouterCour(note(2, '2', 15))
        print(dataBase.editerCours(nouIntCours=coursUn,nouNivCours='2'))
        print(db.noteCoursImp(coursUn))
        print(db.noteCoursImp(coursDeux))

