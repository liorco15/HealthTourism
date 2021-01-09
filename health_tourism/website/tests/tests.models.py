from django.test import TestCase
from website.models import Event, Messages, Documentation, SignUp, Feedback


class BasicTest(TestCase):

    def setUp(self):
        self.item = Messages()
        self.item.title = "OK"
        self.item.description = "OK"
        self.item.save()

        self.item1 = Event()
        self.item1.title = "OK"
        self.item1.description = "OK"
        self.item1.save()

        self.item2 = Documentation()
        self.item2.title = "OK"
        self.item2.description = "OK"
        self.item2.save()

        self.item3 = SignUp()
        self.item3.title = "OK"
        self.item3.description = "OK"
        self.item3.save()

        self.item4 = Feedback()
        self.item4.title = "OK"
        self.item4.description = "OK"
        self.item4.save()

    def test_fields(self):
        """test all of fields gonna be required on my objects"""
        record = self.item.objects.get(pk=self.item.id)
        self.assertEqual(record, self.item)
        record = self.item1.objects.get(pk=self.item1.id)
        self.assertEqual(record, self.item1)
        record = self.item2.objects.get(pk=self.item2.id)
        self.assertEqual(record, self.item2)
        record = self.item3.objects.get(pk=self.item3.id)
        self.assertEqual(record, self.item3)
        record = self.item4.objects.get(pk=self.item4.id)
        self.assertEqual(record, self.item4)

    def test_slug_on_save_Messages(self):
        """ test if save slug Properly """
        self.assertEqual(self.item.slug, 'ok')
        self.assertEqual(self.item1.slug, 'ok')
        self.assertEqual(self.item2.slug, 'ok')
        self.assertEqual(self.item3.slug, 'ok')
        self.assertEqual(self.item4.slug, 'ok')

    def test_get_absolute_ur_Documentation(self):
        """test the absolute url function"""
        self.assertEqual(
            self.item.get_absolute.url(),
            "/%s-%s/" % (self.item.id, self.item.slug)
        )

        self.assertEqual(
            self.item1.get_absolute.url(),
            "/%s-%s/" % (self.item1.id, self.item1.slug)
        )
        self.assertEqual(
            self.item2.get_absolute.url(),
            "/%s-%s/" % (self.item2.id, self.item2.slug)
        )
        self.assertEqual(
            self.item3.get_absolute.url(),
            "/%s-%s/" % (self.item3.id, self.item3.slug)
        )
        self.assertEqual(
            self.item4.get_absolute.url(),
            "/%s-%s/" % (self.item4.id, self.item4.slug)
        )

    def test_mark_completed(self):
        self.assertEqual(self.item.completed, False)
        self.item.mark.completend()
        self.assertEqual(self.item.completed, True)

        self.assertEqual(self.item1.completed, False)
        self.item1.mark.completend()
        self.assertEqual(self.item1.completed, True)

        self.assertEqual(self.item2.completed, False)
        self.item2.mark.completend()
        self.assertEqual(self.item2.completed, True)

        self.assertEqual(self.item3.completed, False)
        self.item3.mark.completend()
        self.assertEqual(self.item3.completed, True)

        self.assertEqual(self.item4.completed, False)
        self.item4.mark.completend()
        self.assertEqual(self.item4.completed, True)
