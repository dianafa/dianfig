import urllib2
import re
from bs4 import BeautifulSoup as bs

contributions = [
	[258823,	1679924,	1669300,	9577],
	[290642,	1679927,	1678859,	1003],
	[3847,		1679928,	1679755,	15157],
	[290642,	1679930,	1679927,	1020],
	[2096,		1679931,	1676613,	43570],
	[352431,	1679933,	1678867,	554],
	[23682,		1679934,	1553490,	19842],
	[364005,	1679935,	1499216,	2045],
	[246236,	1679938,	1674934,	1858],
	[32939,		1679939,	1646078,	7429],
	[101287,	1679940,	1579333,	3976],
]

class Contribution(object):
	def __init__(self, page_id, rev_id, rev_parent_id, article_len):
		self.page_id = page_id
		self.rev_id = rev_id
		self.rev_parent_id = rev_parent_id
		self.article_len = article_len
		self.diffpage_url = 'http://disney.diana.wikia-dev.pl/index.php?curid=' + str(page_id) + '&diff=' + str(rev_id) + '&oldid=' + str(rev_parent_id)
		self.html = ''
		self.added_text = ''
		self.removed_text = ''
		print '\n\n' + self.diffpage_url

	def set_html(self, html):
		self.html = html

	def get_html(self):
		if (self.html):
			return self.html

		f = urllib2.urlopen(self.diffpage_url)
		self.set_html(bs(f, "html.parser"))
		return self.html

	def set_added_text(self, text):
		self.added_text = text

	def get_added_text(self):

		added = ''
		for addedline in self.get_html().findAll("td", { "class" : "diff-addedline" }):
			added += addedline.get_text()

		print 'Added: \n' + added
		self.set_added_text(added)
		return added

	def set_removed_text(self, text):
		self.removed_text = text

	def get_removed_text(self):
		if (self.removed_text):
			return self.removed_text

		removed = ''

		for deletedline in self.get_html().findAll("td", { "class" : "diff-deletedline" }):
			removed += deletedline.get_text()

		print 'Removed: \n' + removed
		self.set_removed_text(removed)
		return removed

	def count_images(self):
		print '[[File::';
		print '.jpg, .png';

	def get_added_links_count(self):
		links_in_added = re.findall('\[\[(.*?)\]\]', self.get_added_text())
		links_in_removed = re.findall('\[\[(.*?)\]\]', self.get_removed_text())

		return len(links_in_added) - len(links_in_removed)

	def get_size_delta(self):
		'''
		Including whitespaces
		'''
		addedCount = len(self.get_added_text())
		removedCount = len(self.get_removed_text())

		return addedCount - removedCount

#url = 'http://disney.diana.wikia-dev.pl/index.php?curid=258823&diff=1679924&oldid=1669300'


for contribution in contributions:
	c = Contribution(contribution[0],contribution[1],contribution[2],contribution[3])
	#c.getText()
	print(c.get_size_delta())
	print(c.get_added_links_count())

